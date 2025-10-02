# app.py
from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from utils.core import handle_manual_input
import os
from datetime import datetime
import json

# File to store visitor counts
VISITOR_COUNT_FILE = os.path.join(os.path.dirname(__file__), "Data", "visitor_count.json")

def increment_visitor_count():
    """Increment the visitor count for the current day and total count."""
    # Ensure the directory exists
    os.makedirs(os.path.dirname(VISITOR_COUNT_FILE), exist_ok=True)

    # Load existing data or initialize
    if os.path.exists(VISITOR_COUNT_FILE):
        with open(VISITOR_COUNT_FILE, "r", encoding="utf-8") as file:
            visitor_data = json.load(file)
    else:
        visitor_data = {"total": 0}

    # Get today's date
    today = datetime.now().strftime("%Y-%m-%d")

    # Increment the count for today
    if today in visitor_data:
        visitor_data[today] += 1
    else:
        visitor_data[today] = 1

    # Increment total count
    visitor_data["total"] = visitor_data.get("total", 0) + 1

    # Save the updated data
    with open(VISITOR_COUNT_FILE, "w", encoding="utf-8") as file:
        json.dump(visitor_data, file, indent=4)

app = FastAPI()

# Increment visitor count on every request
@app.middleware("http")
async def add_visitor_count(request: Request, call_next):
    increment_visitor_count()
    response = await call_next(request)
    return response

# Allow frontend to access backend (CORS config)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for dev; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/calculate")
def calculate(
    start_surah: int = Query(..., description="Start Surah number"),
    start_ayah: int = Query(..., description="Start Ayah number"),
    end_surah: int = Query(..., description="End Surah number"),
    end_ayah: int = Query(..., description="End Ayah number")
):
    result = handle_manual_input(start_surah, start_ayah, end_surah, end_ayah)
    
    if "error" in result:
        return {"error": result["error"]}
    
    return {
        "total_ayahs": result["total_ayahs"],
        "hasanat": result["hasanat"]
    }

@app.post("/api/suggestions")
async def save_suggestion(request: Request):
    data = await request.json()
    suggestion = data.get("suggestion", "").strip()

    if not suggestion:
        return {"error": "Suggestion cannot be empty."}

    suggestions_dir = os.path.join(os.path.dirname(__file__), "Data", "Suggestions")
    os.makedirs(suggestions_dir, exist_ok=True)

    suggestion_file = os.path.join(suggestions_dir, "suggestions.txt")
    with open(suggestion_file, "a", encoding="utf-8") as file:
        file.write(suggestion + "\n")

    return {"message": "Suggestion saved successfully."}

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Serve the static folder (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at the root URL
@app.get("/")
def serve_index():
    return FileResponse("static/index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
