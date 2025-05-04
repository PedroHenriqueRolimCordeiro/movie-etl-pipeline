import os
import requests
from dotenv import load_dotenv

# Carrega o token do .env
load_dotenv()
TOKEN = os.getenv("TMDB_BEARER_TOKEN")  # Lê a variável de ambiente

# Configuração da requisição
url = "https://api.themoviedb.org/3/authentication"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"  # Insere o token dinamicamente
}

# Faz a requisição
response = requests.get(url, headers=headers)

# Verifica a resposta
if response.status_code == 200:
    print("Autenticação válida!")
    print("Detalhes:", response.json())
else:
    print("Erro na autenticação:", response.text)