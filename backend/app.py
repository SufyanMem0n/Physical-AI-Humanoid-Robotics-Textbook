import os
import logging
from dotenv import load_dotenv
import cohere
import openai
from qdrant_client import QdrantClient
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional

# --- Custom Modules --- 
# Make sure ingest_content.py is in the same directory or accessible
from ingest_content import ingest_all_book_content, logger as ingest_logger

# --- Environment and Logging Configuration ---
load_dotenv(dotenv_path='.env', override=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- FastAPI App Initialization ---
app = FastAPI(
    title="AI Native Book RAG API",
    description="An API for querying a robotics book using a RAG pipeline and for managing content ingestion.",
    version="1.0.0"
)

# --- CORS Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# --- Configuration from .env ---
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL", "embed-english-v3.0")
LLM_MODEL_NAME = os.getenv("LLM_MODEL", "mistralai/devstral-2512:free")
TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", "7"))
COLLECTION_NAME = "book_content"

# --- Client Initialization ---
try:
    if not all([OPENROUTER_API_KEY, COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY]):
        missing_keys = [key for key, value in {
            "OPENROUTER_API_KEY": OPENROUTER_API_KEY,
            "COHERE_API_KEY": COHERE_API_KEY,
            "QDRANT_URL": QDRANT_URL,
            "QDRANT_API_KEY": QDRANT_API_KEY
        }.items() if not value]
        logger.error(f"Missing environment variables: {', '.join(missing_keys)}")
        raise RuntimeError(f"Missing environment variables: {', '.join(missing_keys)}")

    client = openai.OpenAI(base_url="https://openrouter.ai/api/v1", api_key=OPENROUTER_API_KEY)
    co = cohere.Client(COHERE_API_KEY)
    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
except RuntimeError as e:
    # This will prevent the app from starting if keys are missing
    logger.critical(e)
    # In a real app, you might want a more graceful shutdown or handling
    exit(1)


# --- Pydantic Models for API Data Validation ---
class ChatRequest(BaseModel):
    question: str = Field(..., description="The user's question to be answered.")
    selected_text: Optional[str] = Field(None, description="Optional selected text from the frontend.")

class IngestResponse(BaseModel):
    status: str
    message: str

class ChatResponse(BaseModel):
    response: str


# --- Helper Functions (adapted for FastAPI) ---
def get_embedding(text: str) -> Optional[List[float]]:
    """Generates an embedding for the given text using Cohere."""
    try:
        response = co.embed(texts=[text], model=EMBEDDING_MODEL_NAME, input_type="search_query")
        return response.embeddings[0]
    except Exception as e:
        logger.error(f"Error generating embedding: {e}")
        return None

def retrieve_context(query_embedding: List[float]) -> List[str]:
    """Retrieves relevant context from Qdrant."""
    try:
        search_result = qdrant_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=TOP_K_RESULTS,
        )
        return [hit.payload["content"] for hit in search_result]
    except Exception as e:
        logger.error(f"Error retrieving context from Qdrant: {e}")
        return []

def generate_llm_response(query: str, context: List[str]) -> str:
    """Generates a response using the LLM based on the query and context."""
    context_str = "\n".join(context) if context else "No context found."
    system_prompt = """You are a professional and knowledgeable AI assistant for an industry course on Physical AI & Humanoid Robotics.
    Answer the user's question based ONLY on the provided context from the course material.
    If the answer cannot be found in the context, state that clearly and suggest looking into related chapters."""
    user_prompt = f"Course Material Context:\n{context_str}\n\nUser Question: {query}\n\nPlease provide a detailed, professional, and industry-focused answer."

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error generating LLM response: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to generate a response from the language model.")


# --- API Endpoints ---
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Handles the chat request by generating an embedding, retrieving context,
    and generating a response from the language model.
    """
    logger.info(f"Received question: {request.question}")
    
    query_embedding = get_embedding(request.question)
    if not query_embedding:
        raise HTTPException(status_code=500, detail="Failed to generate query embedding.")

    context = retrieve_context(query_embedding)
    logger.info(f"Retrieved {len(context)} context chunks.")

    bot_response = generate_llm_response(request.question, context)
    
    return {"response": bot_response}


def run_ingestion():
    """Wrapper function to run the ingestion process."""
    try:
        # Resolve the absolute path to the 'my-robotics-book/docs' directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
        docs_directory = os.path.join(project_root, "my-robotics-book", "docs")
        
        if not os.path.isdir(docs_directory):
            ingest_logger.error(f"Docs directory not found at the expected path: {docs_directory}")
            return

        ingest_logger.info("Starting background ingestion process...")
        ingest_all_book_content(docs_directory)
        ingest_logger.info("Background ingestion process finished.")
    except Exception as e:
        ingest_logger.error(f"An error occurred during background ingestion: {e}", exc_info=True)


@app.post("/ingest", response_model=IngestResponse)
async def trigger_ingestion(background_tasks: BackgroundTasks):
    """
    Triggers the content ingestion process as a background task.
    This allows the API to immediately return a response while ingestion runs.
    """
    logger.info("Ingestion endpoint called. Scheduling ingestion as a background task.")
    background_tasks.add_task(run_ingestion)
    return {
        "status": "success",
        "message": "Content ingestion has been scheduled to run in the background."
    }

# --- To run this app locally, use uvicorn: ---
# uvicorn app:app --reload
# For example, if you save this as app.py, run the command above in your terminal.
