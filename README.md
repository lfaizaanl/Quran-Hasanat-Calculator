# Quran Hasanat Calculator(https://guided-mostly-serval.ngrok-free.app)

A FastAPI-based backend for calculating hasanat (rewards) from Quran ayahs, tracking visitor counts, and collecting user suggestions. Includes a simple frontend served as static files.

## Features
- Calculate total ayahs and hasanat between any two ayah ranges
- Track daily and total visitor counts
- Collect user suggestions
- Serve a static frontend (HTML, JS, CSS)
- CORS enabled for frontend-backend communication

## Project Structure
```
Backend/
  app.py                # Main FastAPI app
  utils/                # Core logic and parsers
  static/               # Frontend (index.html, App.js, style.css)
  Data/                 # Data files (visitor counts, suggestions)
  Archive/              # Old scripts and resources
  resources/            # PDF and other resources
  __pycache__/          # Python cache files

env/                    # Python virtual environment
```

## Requirements
- Python 3.8+
- All dependencies are listed in `requirements.txt`

## Setup
1. Clone the repository
2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv env
   env\Scripts\activate  # On Windows
   source env/bin/activate  # On Linux/Mac
   ```
3. Install all dependencies with one command:
   ```
   pip install -r requirements.txt
   ```
4. Run the backend:
   ```
   cd Backend
   uvicorn app:app --reload
   ```
5. (Optional) Expose with ngrok:
   ```
   ngrok http 8000
   ```

## API Endpoints
- `GET /calculate` — Calculate hasanat for a given ayah range
- `POST /api/suggestions` — Submit a suggestion
- `GET /` — Serve the frontend
- `GET /static/*` — Serve static files

## Notes
- Visitor counts and suggestions are stored in `Backend/Data/`
- Static files are served from `Backend/static/`
- For production, restrict CORS and use a production server

## License
MIT License
