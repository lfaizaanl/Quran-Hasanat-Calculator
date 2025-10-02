import sys
import os

# Add backend root to sys.path for clean utils import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))

from utils.core import handle_text_input, handle_manual_input

def main():
    print("Quran Hasanat Range Calculator")
    print("1. Enter range like '2:15-3:15'")
    print("2. Enter manual range using Surah & Ayah")

    choice = input("Choose input type (1 or 2): ").strip()

    if choice == '1':
        text = input("Enter range (e.g. 2:15-3:15): ").strip()
        result = handle_text_input(text)

    elif choice == '2':
        try:
            s_start = int(input("Enter starting Surah: "))
            a_start = int(input("Enter starting Ayah: "))
            s_end = int(input("Enter ending Surah: "))
            a_end = int(input("Enter ending Ayah: "))
            result = handle_manual_input(s_start, a_start, s_end, a_end)
        except ValueError:
            print("❌ Please enter valid integers.")
            return
    else:
        print("❌ Invalid choice")
        return

    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        print(f"\n✅ Range: {result['range']}")
        print(f"📖 Total Ayahs: {result['total_ayahs']}")
        print(f"🔠 Total Letters: {result['total_letters']}")
        print(f"✨ Total Hasanat: {result['hasanat']}")

if __name__ == "__main__":
    main()
