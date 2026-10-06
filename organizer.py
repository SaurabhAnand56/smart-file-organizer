import os
import shutil
from pathlib import Path
import sys


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".csv", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def get_category(extension):
    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("❌ Folder does not exist.")
        return

    if not folder.is_dir():
        print("❌ The provided path is not a folder.")
        return

    moved_files = 0

    for file in folder.iterdir():

        if not file.is_file():
            continue

        category = get_category(file.suffix)

        destination = folder / category
        destination.mkdir(exist_ok=True)

        target = destination / file.name

        # Avoid overwriting existing files
        if target.exists():
            stem = file.stem
            suffix = file.suffix
            counter = 1

            while target.exists():
                target = destination / f"{stem}_{counter}{suffix}"
                counter += 1

        shutil.move(str(file), str(target))

        print(f"✓ {file.name} → {category}/")
        moved_files += 1

    print(f"\nDone! Organized {moved_files} file(s).")




if __name__ == "__main__":
    print("📂 Smart File Organizer")
    print("-" * 30)

    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Enter folder path: ").strip()

    organize_folder(folder)