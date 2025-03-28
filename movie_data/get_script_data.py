import os
import time
import json
import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm

IMSD_BASE = "https://www.imsdb.com/scripts"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def normalize_title(title: str) -> str:
    title = title.replace("&", "%2526")
    match = re.match(r'^(The|A|An)\s+(.*)', title, flags=re.IGNORECASE)
    if match:
        title = f"{match.group(2)},-{match.group(1).title()}"
    cleaned = re.sub(r"[^\w\s,%\-]", "", title)
    return "-".join(cleaned.split())


def clean_script_text(text: str) -> str:
    text = text.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")

    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()


def download_script_content(title: str) -> str | None:
    slug = normalize_title(title)
    direct_url = f"https://www.imsdb.com/scripts/{slug}.html"
    resp = requests.get(direct_url, headers=HEADERS)

    if resp.status_code != 200:
        search_url = "https://www.imsdb.com/search.php"
        resp = requests.get(search_url, params={"query": title}, headers=HEADERS)
        soup = BeautifulSoup(resp.text, "html.parser")
        link = soup.select_one("p a[href^='/scripts/']")
        if not link:
            return None
        direct_url = "https://www.imsdb.com" + link["href"]
        resp = requests.get(direct_url, headers=HEADERS)
        if resp.status_code != 200:
            return None

    soup = BeautifulSoup(resp.text, "html.parser")
    content = soup.find("td", class_="scrtext")
    if not content:
        return None

    raw_text = content.get_text("\n")
    return clean_script_text(raw_text)


def main():
    with open("movie_data.json", "r", encoding="utf-8") as f:
        movies = json.load(f)

    success, failed = [], []
    for movie in tqdm(movies, desc="Downloading scripts"):
        title = movie["movie_title"]
        script = download_script_content(title)
        if script:
            movie["script"] = script
            print(f"[✅] {title}")
            success.append(title)
        else:
            movie["script"] = None
            print(f"[❌] {title}")
            failed.append(title)
        time.sleep(1)

    # Save updated JSON with script contents
    with open("movie_data_with_scripts.json", "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)

    print("\n===== Summary =====")
    print(f"✅ : {len(success)}")
    print(f"❌ : {len(failed)}")
    if failed:
        print("Failed titles:", failed)


if __name__ == "__main__":
    main()

