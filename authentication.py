import os
import requests
from dotenv import load_dotenv

def autenticar_tmdb():
    """Verifica a autenticação com a API do TMDB e imprime o resultado."""
    try:
        load_dotenv()
        TOKEN = os.getenv("TMDB_BEARER_TOKEN")
        
        if not TOKEN:
            print("❌ Erro: Token não encontrado")
            return

        response = requests.get(
            "https://api.themoviedb.org/3/authentication",
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {TOKEN}"
            }
        )

        print("✅ Autenticação válida!" if response.status_code == 200 
              else f"❌ Falha: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")