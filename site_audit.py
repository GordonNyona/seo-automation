import requests
from bs4 import BeautifulSoup
import argparse

def audit_site(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No title"
        description = soup.find("meta", attrs={"name": "description"})
        description = description["content"] if description else "No meta description"

        print(f"Site: {url}")
        print(f"Title: {title}")
        print(f"Meta Description: {description}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Website URL to audit")
    args = parser.parse_args()

    audit_site(args.url)
