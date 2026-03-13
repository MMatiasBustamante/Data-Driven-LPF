import os
import requests as rq
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY") # Tu nueva clave de Football-Data

# Probamos con la Premier League o ligas europeas que son las fijas del plan gratuito
# (Después buscamos el ID de la Argentina)
url = "https://api.football-data.org/v4/competitions/PL/teams"

headers = {
    'X-Auth-Token': API_KEY  # Este es el formato que usa esta API
}

def probar_nueva_api():
    print("Intentando con Football-Data.org...")
    response = rq.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("¡CONECTADO!")
        for team in data['teams'][:5]: # Mostramos los primeros 5
            print(f"- {team['name']} ({team['venue']})")
    else:
        print(f"Error {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    probar_nueva_api()