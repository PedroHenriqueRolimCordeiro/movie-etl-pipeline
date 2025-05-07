import os
import requests
import time
from dotenv import load_dotenv
from authentication import autenticar_tmdb  

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Realiza autenticação
autenticar_tmdb()

BASE_URL = "https://api.themoviedb.org/3"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")


def discover_movies(year, sort_by, vote_count_min=50, lang_filter=None, max_filmes=500):
    films = []
    page = 1
    while len(films) < max_filmes:
        params = {
            "api_key": TMDB_API_KEY,
            "primary_release_year": year,
            "sort_by": sort_by,
            "vote_count.gte": vote_count_min,
            "language": "pt-BR",
            "page": page
        }
        if lang_filter:
            params["with_original_language"] = lang_filter

        resp = requests.get(f"{BASE_URL}/discover/movie", params=params)
        if resp.status_code != 200:
            break

        data = resp.json()
        results = data.get("results", [])
        if not results:
            break

        films.extend(results)
        if page >= data.get("total_pages", 1):
            break
        page += 1
        time.sleep(0.25)

    return films[:max_filmes]  # <-- fora do while

    

# Busca filmes populares de 2023 em português
filmes = discover_movies(year=2023, sort_by="popularity.desc")
print(f"Total de filmes: {len(filmes)}")
print(f"Exemplo: {filmes[0]['title']} (Nota: {filmes[0]['vote_average']})")