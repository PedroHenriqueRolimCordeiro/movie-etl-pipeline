import os
import requests
from dotenv import load_dotenv
from authentication import *

load_dotenv()
autenticar_tmdb()

BASE_URL =" https://api.themoviedb.org/3"
TMDB_API_KEY = os.getenv("TMDB_API_KEY")


def get_movies_per_year(year, page=1):  #Vai gerar isso aqui ?api_key=SUA_CHAVE&primary_release_year=2020&page=1&language=pt-BR  
    url=f"{BASE_URL}/discover/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "primary_release_year": year,
        "page": page,
        "language": "pt-BR" #obter os dados em portugues
    }
    response = requests.get(url, params=params)
    return response.json()

movies_2000 = get_movies_per_year(2000)
print(movies_2000)