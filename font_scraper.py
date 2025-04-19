import os
import json
import uuid
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from rich.progress import track

HEADERS = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

BASE_URL = "https://www.dafont.com"
FONT_DIR = "fonts"
os.makedirs(FONT_DIR, exist_ok=True)

all_fonts = []

def download_image(url, save_path):
    try:
        r = requests.get(url, headers=HEADERS, stream=True, timeout=10)
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        print(f"❌ Failed to download image {url} → {e}")

def parse_page(url):
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.content, 'html.parser')
    fonts = soup.find_all('div', class_='dlbox')

    for font in fonts:
        try:
            title = font.a['title']
            font_link = 'https:' + font.a['href']
            img_url = BASE_URL + font.find_next_sibling('div')['style'].split('(')[1].split(')')[0]

            font_id = str(uuid.uuid4())
            img_path = os.path.join(FONT_DIR, f"{font_id}.png")

            # Download image
            download_image(img_url, img_path)

            font_data = {
                "id": font_id,
                "title": title,
                "font_link": font_link,
                "font_image": f"{font_id}.png"
            }

            all_fonts.append(font_data)
        except Exception as e:
            print(f"❌ Error parsing font → {e}")

def get_all_page_links(letter):
    url = f"{BASE_URL}/alpha.php?lettre={letter}"
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        last_page = int(soup.find('div', class_='noindex').find_all('a')[-2].text)
    except:
        last_page = 1
    return [f"{BASE_URL}/alpha.php?lettre={letter}&page={i}" for i in range(1, last_page + 1)]

def scrape_all():
    letters = 'abcdefghijklmnopqrstuvwxyz%23'
    for letter in letters:
        page_links = get_all_page_links(letter)
        for link in track(page_links, description=f"[green]Scraping {letter.upper()}..."):
            parse_page(link)

    # Save full JSON
    with open(os.path.join(FONT_DIR, 'fonts_db.json'), 'w') as f:
        json.dump(all_fonts, f, indent=2)

    print(f"\n✅ Finished! Saved {len(all_fonts)} fonts into fonts_db.json")

if __name__ == "__main__":
    scrape_all()
