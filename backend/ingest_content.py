import os
import glob
import uuid
from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from qdrant_client.http.exceptions import UnexpectedResponse
import logging
from typing import List, Dict, Any

# Load environment variables from .env file
load_dotenv(dotenv_path='.env', override=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Configuration from .env or environment variables ---
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY") 
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL", "embed-english-v3.0")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "700"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))

# --- Initialize Clients ---
if not COHERE_API_KEY:
    logger.error("COHERE_API_KEY not found. Please set it in your .env file.")
    exit(1)
if not QDRANT_URL:
    logger.error("QDRANT_URL not found. Please set it in your .env file.")
    exit(1)
if not QDRANT_API_KEY:
    logger.error("QDRANT_API_KEY not found. Please set it in your .env file.")
    exit(1)

co = cohere.Client(COHERE_API_KEY)
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Define Qdrant collection name
COLLECTION_NAME = "book_content"

# --- Text Preprocessing and Chunking (Simple Markdown Parser) ---
def chunk_text(text: str, file_path: str) -> List[Dict[str, Any]]:
    """
    Splits text into chunks of a specified size with overlap,
    and extracts metadata from the file path.
    """
    chunks = []
    current_chunk = ""
    current_chunk_length = 0
    
    # Basic metadata from file path
    path_parts = file_path.split(os.sep)
    book_part = None
    chapter_title = None

    if "Part-I-Foundations" in path_parts:
        book_part = "Part I: Foundations"
    elif "Part-II-Digital-Twins" in path_parts:
        book_part = "Part II: Digital Twins"
    elif "Part-III-NVIDIA-Isaac" in path_parts:
        book_part = "Part III: NVIDIA Isaac"
    elif "Part-IV-VLA-Humanoid" in path_parts:
        book_part = "Part IV: VLA & Humanoid"
    
    file_name = os.path.basename(file_path).replace(".md", "").replace(".mdx", "")
    # Attempt to get a more readable chapter title
    chapter_title = file_name.replace("-", " ").title()
    if chapter_title.startswith("Week "):
        chapter_title = chapter_title.replace("Week ", "Week ").replace(" Introduction To ", ": Introduction to ").replace(" Ros 2 ", ": ROS 2 ")


    for paragraph in text.split('\n\n'): # Split by paragraphs for better chunking
        if not paragraph.strip():
            continue
        
        # If adding the next paragraph exceeds chunk size, create a new chunk
        if current_chunk_length + len(paragraph) + 2 > CHUNK_SIZE: # +2 for newline
            if current_chunk:
                chunks.append({
                    "content": current_chunk.strip(),
                    "source_file": file_path,
                    "book_part": book_part,
                    "chapter_title": chapter_title
                })
                # For overlap, take the last part of the current chunk
                current_chunk = current_chunk[max(0, len(current_chunk) - CHUNK_OVERLAP):] + "\n\n" + paragraph
                current_chunk_length = len(current_chunk)
            else: # If a single paragraph is too large
                # Force chunking by character if paragraph is too long
                for i in range(0, len(paragraph), CHUNK_SIZE - CHUNK_OVERLAP):
                    sub_chunk = paragraph[i : i + CHUNK_SIZE]
                    chunks.append({
                        "content": sub_chunk.strip(),
                        "source_file": file_path,
                        "book_part": book_part,
                        "chapter_title": chapter_title
                    })
                current_chunk = paragraph[max(0, len(paragraph) - CHUNK_OVERLAP):]
                current_chunk_length = len(current_chunk)
        else:
            current_chunk += paragraph + "\n\n"
            current_chunk_length += len(paragraph) + 2
    
    if current_chunk:
        chunks.append({
            "content": current_chunk.strip(),
            "source_file": file_path,
            "book_part": book_part,
            "chapter_title": chapter_title
        })

    return chunks

def get_embeddings_for_chunks(chunks: List[Dict[str, Any]]) -> List[List[float]]:
    """Generates embeddings for a list of text chunks."""
    texts = [chunk["content"] for chunk in chunks]
    try:
        response = co.embed(texts=texts, model=EMBEDDING_MODEL_NAME, input_type="search_document")
        return response.embeddings
    except Exception as e:
        logger.error(f"Error generating embeddings for {len(texts)} chunks: {e}")
        return []

# A consistent namespace for generating UUIDs
NAMESPACE_UUID = uuid.UUID('f2b4e2c8-4235-4a53-9a74-419b334a9b70') # A random but fixed UUID

def upsert_chunks_to_qdrant(chunks_with_embeddings: List[Dict[str, Any]]):
    """Upserts chunks and their embeddings to Qdrant."""
    points = []
    for i, chunk_data in enumerate(chunks_with_embeddings):
        # Generate a deterministic UUIDv5 from the content and file path
        point_id = str(uuid.uuid5(NAMESPACE_UUID, chunk_data["content"] + chunk_data["source_file"]))
        points.append(
            PointStruct(
                id=point_id,
                vector=chunk_data["embedding"],
                payload={
                    "content": chunk_data["content"],
                    "source_file": chunk_data["source_file"],
                    "book_part": chunk_data["book_part"],
                    "chapter_title": chunk_data["chapter_title"]
                }
            )
        )
    
    if points:
        try:
            # Upsert in batches
            batch_size = 100
            for i in range(0, len(points), batch_size):
                batch_points = points[i:i+batch_size]
                qdrant_client.upsert(
                    collection_name=COLLECTION_NAME,
                    wait=True,
                    points=batch_points
                )
                logger.info(f"Upserted {len(batch_points)} points to Qdrant.")
        except Exception as e:
            logger.error(f"Error upserting points to Qdrant: {e}")

def create_qdrant_collection_if_not_exists():
    """Creates the Qdrant collection if it does not already exist."""
    try:
        # Check if collection already exists
        collections = qdrant_client.get_collections().collections
        if COLLECTION_NAME in [c.name for c in collections]:
            logger.info(f"Collection '{COLLECTION_NAME}' already exists. Skipping creation.")
            return

        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=1024, distance=Distance.COSINE), # Cohere embed-english-v3.0 is 1024 dim
        )
        logger.info(f"Collection '{COLLECTION_NAME}' created successfully.")
    except Exception as e:
        logger.error(f"Error creating Qdrant collection: {e}")
        exit(1)


def ingest_all_book_content(docs_dir: str):
    """
    Ingests all Markdown content from the specified directory into Qdrant.
    """
    create_qdrant_collection_if_not_exists()
    
    markdown_files = glob.glob(os.path.join(docs_dir, "**/*.md"), recursive=True)
    markdown_files.extend(glob.glob(os.path.join(docs_dir, "**/*.mdx"), recursive=True))
    
    if not markdown_files:
        logger.warning(f"No Markdown files found in {docs_dir}. Qdrant collection will be empty.")
        return

    all_chunks_to_embed = []
    for file_path in markdown_files:
        logger.info(f"Processing file: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            chunks = chunk_text(content, file_path)
            all_chunks_to_embed.extend(chunks)
        except Exception as e:
            logger.error(f"Error reading or chunking file {file_path}: {e}")
            continue

    if not all_chunks_to_embed:
        logger.warning("No chunks generated from any files. Nothing to embed or upsert.")
        return

    logger.info(f"Total {len(all_chunks_to_embed)} chunks generated across all files. Generating embeddings...")
    embeddings = get_embeddings_for_chunks(all_chunks_to_embed)

    if len(embeddings) != len(all_chunks_to_embed):
        logger.error("Mismatch between number of chunks and embeddings. Aborting upsert.")
        return

    chunks_with_embeddings = []
    for i, chunk in enumerate(all_chunks_to_embed):
        chunk["embedding"] = embeddings[i]
        chunks_with_embeddings.append(chunk)

    logger.info(f"Upserting {len(chunks_with_embeddings)} chunks with embeddings to Qdrant...")
    upsert_chunks_to_qdrant(chunks_with_embeddings)
    logger.info("Content ingestion complete.")
