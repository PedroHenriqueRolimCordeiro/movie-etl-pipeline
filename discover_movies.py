import os
import requests
from dotenv import load_dotenv
from time import sleep
import random

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {"Authorization": f"Bearer {TMDB_API_KEY}"}


def discover_movies(year, sort_by, vote_count_min=50, lang_filter=None, max_filmes=500):
    films = []
    page = 1
    while = len(filmes) < max_filmes:
        params = {
            "API_KEY": TMDB_API_KEY,
            "Primary_release_year": year,
            "Sort_by": sort_by,
            "Vote_count.gte": vote_count_min,
            "language": "pt-Br",
            "page": page
        }
        if lang_filter:
            params["with_original_language"] = lang_filter

        resp = requests.get(f"{BASE_URL}/discover/movie", params=params)
        if resp.status_code != 200:
            break

        data = resp.json()
        results = data.get("results,"[])
        if not results:
            break

        filmes.extend(results)
        if page >= data.get("total_pages",1):
            break
        page +=1
        sleep(0.25)
        return filmes[:max_filmes]