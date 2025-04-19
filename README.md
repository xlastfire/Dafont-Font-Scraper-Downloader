
---

```markdown
# 🖋️ Dafont Font Scraper & Downloader

This project helps you **scrape fonts from [Dafont.com](https://www.dafont.com)**, preview their images, and selectively download only the font files (`.zip`). It's built in two parts:

- `font_scraper.py` — Scrapes all fonts and saves metadata + preview images.
- `font_downloader.py` — Downloads only selected `.zip` font files.

---

## 📁 Project Structure

```
project/
│
├── font_scraper.py           🕸️ Script to scrape font data & preview images
├── font_downloader.py        📥 Script to download selected .zip font files
├── fonts/                    📂 Folder containing:
│   ├── fonts_db.json         📑 Font database with metadata + UUIDs
│   ├── <uuid>.png            🖼️ Preview images for each font
│   └── <uuid>.zip            🗂️ Downloaded zip files (after running downloader)
│
└── downloader.log            📜 Download log file
```

---

## 🛠️ Requirements

Install required packages with:

```bash
pip install requests beautifulsoup4 html5lib rich
```

---

## 🚀 How to Use

### 📌 STEP 1: Scrape Font Metadata + Images

Run the scraper to collect font data and preview images:

```bash
python font_scraper.py
```

✔️ This will:

- Scrape all fonts (A-Z and #)
- Save **preview image** (`.png`) into the `fonts/` folder
- Save metadata and download links into `fonts/fonts_db.json`
- Assign a unique UUID to each font entry

---

### 🖼️ STEP 2: Filter Fonts (Optional)

After scraping:

- Open the `fonts/` folder
- **Manually delete** any preview images you don't want
- Only fonts with their image (`.png`) remaining will be downloaded

> 🔒 `font_downloader.py` will download only those fonts that still have preview images.

---

### 📌 STEP 3: Download Font `.zip` Files

Run the downloader to fetch zip files of the selected fonts:

```bash
python font_downloader.py
```

✔️ This will:

- Load the `fonts_db.json` file
- Skip already downloaded `.zip` files
- Match `.png` previews and download `.zip` font files
- Log actions in `downloader.log`
- Show beautiful emoji-rich progress bars 🚀

---

## ✅ Features

- 🧠 Intelligent UUID-based naming
- 🧵 Multithreaded scraping and downloading with `concurrent.futures`
- 📸 Saves font previews as images
- 📂 Stores everything in one clean `fonts/` folder
- 📜 Logging enabled
- 🖼️ Manual filtering of fonts made easy
- ⚡ Skips already downloaded files
- 🎨 Emoji-rich feedback with `rich.progress`

---

## 📦 File Naming Convention

Each font is saved using a unique ID:

| File Type    | Format                |
|--------------|------------------------|
| Preview      | `fonts/<uuid>.png`     |
| Font ZIP     | `fonts/<uuid>.zip`     |
| Metadata     | `fonts/fonts_db.json`  |

---

## 🧠 Example Workflow

1. Run `font_scraper.py` → generates all preview images & font metadata.
2. Delete unwanted images from `fonts/`.
3. Run `font_downloader.py` → downloads `.zip` files only for your chosen ones.

---

## 💡 Tips

- You can stop & restart the process safely.
- Already downloaded `.zip` and `.png` files will be skipped.
- Customize scraping or filtering logic using UUIDs or metadata.

---

## 👨‍💻 Author

Created with ❤️ to give you full control over your font collections from [Dafont.com](https://www.dafont.com).

---

## 📃 License

This project is for personal use and educational purposes only. Please respect the licensing of fonts on Dafont before using them in commercial work.

---
```
