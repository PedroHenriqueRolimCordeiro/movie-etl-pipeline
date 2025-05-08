import requests
import time
from config import TMDB_API_KEY, BASE_URL

def discover_movies(year, sort_by="popularity.desc", vote_count_gte=0, original_language=None, max_pages=5):
    filmes = []
    for page in range(1, max_pages + 1):
        url = f"{BASE_URL}/discover/movie"
        params = {
            "api_key": TMDB_API_KEY,
            "primary_release_year": year,
            "sort_by": sort_by,
            "vote_count.gte": vote_count_gte,
            "language": "pt-BR",
            "page": page
        }
        if original_language:
            params["with_original_language"] = original_language

        response = requests.get(url, params=params)
        if response.status_code != 200:
            break

        data = response.json()
        filmes.extend(data.get("results", []))
        if page >= data.get("total_pages", 1):
            break
        time.sleep(0.25)
    
    return filmes

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR", "append_to_response": "credits"}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    diretor = None
    for pessoa in data.get("credits", {}).get("crew", []):
        if pessoa.get("job") == "Director":
            diretor = pessoa.get("name")
            break

    from transform import calcular_roi

    return {
        "id": data.get("id"),
        "titulo": data.get("title"),
        "ano_lancamento": data.get("release_date", "")[:4],
        "generos": [g["name"] for g in data.get("genres", [])],
        "diretor": diretor,
        "orcamento": data.get("budget"),
        "bilheteria": data.get("revenue"),
        "roi": calcular_roi(data.get("budget"), data.get("revenue")),
        "avaliacao": data.get("vote_average"),
        "votos": data.get("vote_count"),
        "popularidade": data.get("popularity"),
        "duracao": data.get("runtime"),
        "adulto": data.get("adult"),
        "status": data.get("status"),
        "linguas": [l["name"] for l in data.get("spoken_languages", [])],
        "paises": [p["name"] for p in data.get("production_countries", [])],
        "distribuidora": data.get("production_companies", [{}])[0].get("name")
    }
