
from datetime import datetime, timezone
import requests
import json
import sys
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la API de JumpCloud
API_BASE_URL = "https://api.jumpcloud.com"
API_KEY = os.getenv('API_KEY')   # API de Admin en Jumpcloud

# Encabezados de autenticación
headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

def get_user_login_attempts(start_time, end_time):
    """
    Obtiene logs de cuando se loguea un usuario
    """
    url = f"{API_BASE_URL}/insights/directory/v1/events"

    body = {
        "service" : [
            "directory"
        ],
        "start_time" : f"{start_time}",
        "end_time": f"{end_time}",

        "search_term": {
            "or": {
                "event_type": "admin_login_attempt",
                "event_type": "user_login_attempt"
            }
        }
    }

    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code == 200:
        eventos = response.json()
        # Guardo los resultados en un JSON
        with open('login_attempts.json', 'w') as f:
            json.dump(eventos, f, indent=4)
        print("Se han escrito los intentos de inicio de sesion")
        return True
    # Si ha habido un error en la llamada, no se ejecutara el resto del programa
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False


def main():
    # Pongo el rango de fechas desde los que cogeré los logs
    start_time = sys.argv[1]
    end_time = sys.argv[2]
    print(end_time)
    success = get_user_login_attempts(start_time, end_time)
    return success

if __name__ == "__main__":
    main()