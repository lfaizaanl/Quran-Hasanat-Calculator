import json
import re
from pdfplumber import open as open_pdf

def parse_quran_pdf_to_json(pdf_path, output_path):
    extracted_data = []

    with open_pdf(pdf_path) as pdf:
        linear_index = 0  

        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = text.split("\n")
            for line in lines:
                
                nums = re.findall(r"\b\d+\b", line)

                if len(nums) == 5:
                    linear_index = int(nums[0])  
                    surah = int(nums[1])
                    ayah = int(nums[2])
                    words = int(nums[3])
                    letters = int(nums[4])

                    extracted_data.append({
                        "index": linear_index,
                        "surah": surah,
                        "ayah": ayah,
                        "words": words,
                        "letters": letters
                    })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=2)

