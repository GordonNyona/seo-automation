import requests
from bs4 import BeautifulSoup
import csv
import argparse

def scrape_keywords(query, limit=10):
    url = f"https://www.google.com/search?q={query}&num={limit}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for g in soup.find_all("div", class_="tF2Cxc"):
        title = g.find("h3").text if g.find("h3") else "No title"
        link = g.find("a")["href"] if g.find("a") else "No link"
        results.append([title, link])

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keyword scraper")
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Number of results")
    parser.add_argument("--output", type=str, default="results.csv", help="CSV filename")
    args = parser.parse_args()

    print(f"🔎 Scraping Google for: {args.query} (limit {args.limit})...")
    data = scrape_keywords(args.query, args.limit)

    # Save to CSV
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "URL"])
        writer.writerows(data)

    print(f"\n✅ Results saved to {args.output}")
    print("Sample results:")
    for row in data[:5]:
        print(row)
