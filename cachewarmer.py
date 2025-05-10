import feedparser
import requests
from urllib.parse import urlparse
from time import sleep

# Din hemsida och RSS
BASE_URL = "https://www.nordlivpodcast.se"
FEED_URL = f"{BASE_URL}/feed/"
HEADERS = {"User-Agent": "CacheWarmerBot/1.0"}

def visit(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        print(f"Visited {url}: {r.status_code}")
    except Exception as e:
        print(f"Failed to visit {url}: {e}")

def main():
    print("Visiting homepage...")
    visit(BASE_URL)

    print("Fetching RSS feed...")
    feed = feedparser.parse(FEED_URL)
    entries = feed.entries[:10]
    for entry in entries:
        url = entry.link
        print(f"Visiting post: {url}")
        visit(url)
        sleep(2)  # undvik att slå för snabbt

    print("Pinging Google sitemap...")
    sitemap_url = f"{BASE_URL}/sitemap.xml"
    ping_url = f"https://www.google.com/ping?sitemap={sitemap_url}"
    visit(ping_url)

if __name__ == "__main__":
    main()