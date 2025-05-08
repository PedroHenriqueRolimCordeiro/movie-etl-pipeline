import os
import requests
import time
from dotenv import load_dotenv
from authentication import autenticar_tmdb  
from extract import discover_movies
# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Realiza autenticação
autenticar_tmdb()


def test_discover_movies_basic():
    filmes = discover_movies(
        year=2020,
        sort_by="popularity.desc",
        vote_count_gte=100,
        max_pages=1  # Teste leve
    )

    # 1. Deve retornar uma lista
    assert isinstance(filmes, list), "A função deve retornar uma lista."

    # 2. Lista não deve estar vazia
    assert len(filmes) > 0, "A lista de filmes não pode estar vazia."

    # 3. Cada item deve ser um dicionário com chaves esperadas
    required_keys = {"id", "title", "vote_average", "release_date"}
    for filme in filmes:
        assert isinstance(filme, dict), "Cada item deve ser um dicionário."
        assert required_keys.issubset(filme.keys()), f"Faltam chaves esperadas: {required_keys - filme.keys()}"

    print("✅ Teste passou com sucesso!")

if __name__ == "__main__":
    test_discover_movies_basic()
