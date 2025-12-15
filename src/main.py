import markdown
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Base path for the book content
BOOK_CONTENT_PATH = Path("02-parts")

@app.get("/", include_in_schema=False)
async def root():
    """Redirects to the first lesson of the book."""
    return RedirectResponse(url="/book/01-Part-I-Foundations/01-Chapter-Physical-AI/01-Intro")

@app.get("/book/{part_id}/{chapter_id}", response_class=HTMLResponse)
async def read_module_readme(request: Request, part_id: str, chapter_id: str):
    """
    Reads a README.md file from a module directory.
    """
    lesson_path = BOOK_CONTENT_PATH / part_id / chapter_id / "README.md"

    if not lesson_path.exists():
        return HTMLResponse(content="<h1>Module Intro not found</h1>", status_code=404)

    with open(lesson_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content)

    return templates.TemplateResponse("markdown_page.html", {
        "request": request,
        "content": html_content,
        "title": chapter_id.replace('-', ' ').title()
    })

@app.get("/book/{part_id}/{chapter_id}/{lesson_id}", response_class=HTMLResponse)
async def read_lesson(request: Request, part_id: str, chapter_id: str, lesson_id: str):
    """
    Reads a markdown lesson, converts it to HTML, and renders it in a template.
    """
    lesson_path = BOOK_CONTENT_PATH / part_id / chapter_id / f"{lesson_id}.md"

    if not lesson_path.exists():
        return HTMLResponse(content="<h1>Lesson not found</h1>", status_code=404)

    with open(lesson_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content)

    return templates.TemplateResponse("markdown_page.html", {
        "request": request,
        "content": html_content,
        "title": lesson_id.replace('-', ' ').title()
    })
