# 📂 Smart File Organizer

A simple Python utility that automatically organizes files into folders based on their file type.

## ✨ Features

- Automatically categorizes files
- Creates folders when needed
- Supports images, documents, videos, audio, and archives
- Prevents files from being overwritten
- Uses only Python's standard library

## 📁 Example

Before:

```text
Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
├── movie.mp4
└── backup.zip
```

After:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
└── Archives/
    └── backup.zip
```

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/maafiyadon/smart-file-organizer.git
```

Go into the project:

```bash
cd smart-file-organizer
```

Run:

```bash
python organizer.py
```

Enter the path of the folder you want to organize.

## 🛠️ Technologies

- Python 3
- pathlib
- shutil
- os

## 💻 Command Line Usage

You can provide the folder path directly:

```bash
python organizer.py "C:\Users\Saurabh\Downloads"

## 📌 Future Improvements

- Add a dry-run mode
- Add command-line arguments
- Add custom file categories
- Add logging
- Add a graphical interface