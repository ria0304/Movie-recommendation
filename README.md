# 🎬 Movie Recommendation

> Mood-based movie recommendations scraped live from IMDb — no API key needed.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Genres](https://img.shields.io/badge/Genres-5-orange?style=flat-square)
![Results](https://img.shields.io/badge/Results-Top%2014-purple?style=flat-square)

---

## Overview

Movie Recommendation is a lightweight Python CLI tool that takes your current mood as input and returns a curated list of top movies for that genre — scraped in real time from IMDb's feature film charts. No API key, no dataset, no setup beyond two pip packages.

---

## How It Works

1. Takes a mood/genre as input from the user (`Drama`, `Action`, `Comedy`, `Horror`, `Crime`)
2. Maps the mood to a corresponding IMDb genre search URL
3. Sends an HTTP request with a browser-like User-Agent header
4. Parses the HTML response with BeautifulSoup to extract movie titles
5. Strips duplicates and returns the top 14 results

---

## Supported Moods & Genres

| Mood Input | IMDb Genre Scraped |
|---|---|
| `Drama` | Feature films — Drama |
| `Action` | Feature films — Action |
| `Comedy` | Feature films — Comedy |
| `Horror` | Feature films — Horror |
| `Crime` | Feature films — Crime |

> Input is case-insensitive — `drama`, `DRAMA`, and `Drama` all work thanks to `.title()` normalisation.

---

## Technologies Used

| Library | Purpose |
|---|---|
| `requests` | Sends HTTP GET requests to IMDb with a spoofed browser User-Agent |
| `beautifulsoup4` | Parses the HTML and extracts movie title links |
| `lxml` | Fast HTML parser used as BeautifulSoup's backend |
| `re` | Regex pattern to match valid IMDb title URLs (`/title/tt\d+/`) |

---

## Project Structure

```
Movie-recommendation/
│
├── main.py        ← Scraper + CLI entry point
└── README.md      ← Project documentation
```

---

## Installation

### Prerequisites

- Python 3.x
- pip

### Install Dependencies

```bash
pip install requests beautifulsoup4 lxml
```

---

## Usage

```bash
python main.py
```

You'll be prompted to enter a mood:

```
Enter the emotion: Horror
```

The script prints up to 14 movie titles matching that genre from IMDb.

---

## Example Output

```
Enter the emotion: Crime

The Godfather
Goodfellas
The Dark Knight
Pulp Fiction
Schindler's List
The Silence of the Lambs
Léon: The Professional
The Usual Suspects
Se7en
City of God
No Country for Old Men
The Departed
Parasite
Prisoners
```

---

## Error Handling

| Situation | Behaviour |
|---|---|
| Invalid mood entered | Prints `"Invalid emotion"` and exits cleanly |
| IMDb request fails (network/timeout) | Prints the error message and returns an empty list |
| No titles found in parsed HTML | Prints `"No titles found"` |

---

## Limitations

- **IMDb HTML structure may change** — if scraping breaks, the CSS selectors may need updating
- **No pagination** — only scrapes the first IMDb results page (~50 entries before deduplication)
- **5 genres only** — additional moods require adding entries to the `URLS` dictionary

---

## Extending the Project

Adding a new genre takes one line in the `URLS` dictionary:

```python
URLS = {
    ...
    "Romance": 'https://www.imdb.com/search/title/?title_type=feature&genres=romance',
}
```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

