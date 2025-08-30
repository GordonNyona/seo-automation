import requests
from bs4 import BeautifulSoup
import argparse

def scrape_keywords(query, limit=10):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch results")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    results = [h3.get_text() for h3 in soup.find_all("h3")[:limit]]

    print("\nKeyword Suggestions:")
    for idx, keyword in enumerate(results, 1):
        print(f"{idx}. {keyword}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Number of results")
    args = parser.parse_args()

    scrape_keywords(args.query, args.limit)
