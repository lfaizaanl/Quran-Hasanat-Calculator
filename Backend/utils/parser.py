import json
import os

# Load the Quran data once
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'Data', 'quran_ayah_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    AYAH_DATA = json.load(f)

def find_index(surah: int, ayah: int) -> int:
    for idx, entry in enumerate(AYAH_DATA):
        if entry["surah"] == surah and entry["ayah"] == ayah:
            return idx
    raise ValueError(f"Surah {surah}, Ayah {ayah} not found.")

def get_data_by_manual_range(start_surah, start_ayah, end_surah, end_ayah):
    try:
        start_idx = find_index(start_surah, start_ayah)
        end_idx = find_index(end_surah, end_ayah)

        if start_idx > end_idx:
            return {"error": "Starting ayah must come before ending ayah."}

        selection = AYAH_DATA[start_idx:end_idx + 1]
        total_letters = sum(entry["letters"] for entry in selection)

        return {
            "range": f"{start_surah}:{start_ayah}-{end_surah}:{end_ayah}",
            "total_ayahs": len(selection),
            "total_letters": total_letters,
            "hasanat": total_letters * 10
        }
    except ValueError as e:
        return {"error": str(e)}

def get_data_by_text_range(text_range: str):
    try:
        parts = text_range.split("-")
        if len(parts) != 2:
            return {"error": "Range must be in format '2:15-3:5'."}

        start_surah, start_ayah = map(int, parts[0].split(":"))
        end_surah, end_ayah = map(int, parts[1].split(":"))

        return get_data_by_manual_range(start_surah, start_ayah, end_surah, end_ayah)
    except Exception:
        return {"error": "Invalid format. Please use '2:15-3:5'."}
