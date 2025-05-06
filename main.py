import os
import requests
from dotenv import load_dotenv
from authentication import *

autenticar_tmdb()

def procurar_filme(query):
    url=f""