from .parser import get_data_by_text_range, get_data_by_manual_range

def handle_text_input(text_range):
    return get_data_by_text_range(text_range)

def handle_manual_input(start_surah, start_ayah, end_surah, end_ayah):
    return get_data_by_manual_range(start_surah, start_ayah, end_surah, end_ayah)
