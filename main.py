import os
import requests as rq
import pandas as pd
from dotenv import load_dotenv

# 1. Configuración inicial
load_dotenv()
token = os.getenv("API_KEY")
url = "https://api.football-data.org/v4/competitions/PL/teams"

headers = {'X-Auth-Token': token}

def extraer_equipos_premier():
    print("Extrayendo equipos de la Premier League...")
    response = rq.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        equipos_raw = data.get('teams', [])
        
        # 2. Transformación (Data Cleaning)
        # Elegimos solo las columnas que nos interesan para el análisis
        lista_equipos = []
        for team in equipos_raw:
            info = {
                "id_equipo": team['id'],
                "nombre": team['name'],
                "nombre_corto": team['shortName'],
                "tla": team['tla'], # El código de 3 letras (ej: ARS)
                "estadio": team['venue'],
                "fundacion": team['founded'],
                "web": team['website']
            }
            lista_equipos.append(info)
        
        # 3. Creación del DataFrame
        df_equipos = pd.DataFrame(lista_equipos)
        
        # 4. Persistencia (Guardar los datos)
        if not os.path.exists('data'):
            os.makedirs('data')
            
        df_equipos.to_csv("data/equipos_premier.xlsx", index=False)
        
        print(f"Éxito! Se guardaron {len(df_equipos)} equipos.")
        print("\nPrimeros 5 equipos en la tabla:")
        print(df_equipos.head())
        
        return df_equipos
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    df = extraer_equipos_premier()     