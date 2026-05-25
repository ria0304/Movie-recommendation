import requests as r
from bs4 import BeautifulSoup
import re

URLS = {
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
}

def main(emo):
    url = URLS.get(emo)
    if not url:
        print("Invalid emotion")
        return []

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        req = r.get(url, headers=headers)
        req.raise_for_status()
    except r.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    soup = BeautifulSoup(req.text, "lxml")
    titles = [
        a.get_text().strip()
        for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))
    ]

    return list(dict.fromkeys(titles))  # removes duplicates

if __name__ == "__main__":
    emo = input("Enter the emotion: ").strip().title()
    mo = main(emo)

    if not mo:
        print("No titles found")
    else:
        max_titles = 14
        for title in mo[:max_titles]:
            print(title)
