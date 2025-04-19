import os
import json
import requests
import logging
from concurrent.futures import ThreadPoolExecutor
from rich.progress import track

# ========== Setup ==========
FONT_DIR = "fonts"
JSON_FILE = os.path.join(FONT_DIR, "fonts_db.json")
MAX_THREADS = 10

# ========== Logger ==========
logging.basicConfig(
    filename='downloader.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# ========== Load Fonts ==========
with open(JSON_FILE, 'r') as f:
    fonts_data = json.load(f)

# ========== Download One Font ==========
def download_font_zip(font):
    font_id = font['id']
    zip_filename = os.path.join(FONT_DIR, f"{font_id}.zip")
    image_path = os.path.join(FONT_DIR, f"{font_id}.png")

    # Skip if image doesn't exist (user deleted)
    if not os.path.exists(image_path):
        logging.info(f"⛔ Skipping {font_id} – preview image deleted.")
        return

    # Skip if already downloaded
    if os.path.exists(zip_filename):
        logging.info(f"✅ Already downloaded {font_id}")
        return

    # Download .zip
    try:
        r = requests.get(font['font_link'], stream=True, timeout=10)
        r.raise_for_status()

        with open(zip_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        logging.info(f"🎉 Downloaded: {font['title']} ({font_id})")
    except Exception as e:
        logging.error(f"❌ Failed to download {font_id} → {e}")

# ========== Main ==========
def main():
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        list(track(
            executor.map(download_font_zip, fonts_data),
            total=len(fonts_data),
            description="[cyan]Downloading fonts..."
        ))

    print("\n✅ Done downloading all available fonts!")

if __name__ == "__main__":
    main()
