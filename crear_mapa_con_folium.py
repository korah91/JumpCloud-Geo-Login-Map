import json
import sys
import folium
from folium.plugins import MarkerCluster
import pandas as pd

def read_json(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)
    
def create_map(data, start_time, end_time):
    # Crear un mapa centrado en una ubicación
    m = folium.Map(location=[20, 0], zoom_start=2)
    marker_cluster = MarkerCluster().add_to(m)
    # Iterar sobre cada elemento en el json y agregar marcadores en el mapa
    for event in data:
        # Si tiene info sobre geolocalizacion
        if 'geoip' in event:
            geoip = event['geoip']
            lat = geoip.get("latitude")
            lon = geoip.get("longitude")
            # Si tiene datos correctos de geolocalizacion
            if lat and lon:
                # Creo el marcador y lo agrego al mapa
                # Cuando es un usuario el que se loguea, contiene su username. Cuando es admin su email. A veces no hay ni username ni email en la response
                # Se tratan dichas excepciones
                if 'email' in event['initiated_by']:
                    user_info = event['initiated_by']['email']
                elif 'username' in event['initiated_by']:
                    user_info = event['initiated_by']['username']
                else:
                    user_info = event['initiated_by']['id']

                # Si el evento es un inicio de sesion correcto sera un icono verde. Si es incorrecto, rojo
                color = "green" if event['success'] else "red"
                folium.Marker(
                    location=[lat,lon],
                    # Se modifica el timestamp para que quite los milisegundos
                    popup= f"User: {user_info}<br>"
                           f"Event Type: {event.get('event_type')}<br>"
                           f"Success: {event.get('success')}<br>"
                           f"Time: {event.get('timestamp').split('.')[0] + "Z"}",
                    icon = folium.Icon(color=color, icon="info-sign")
                ).add_to(marker_cluster)                

    # Añadir título con las fechas seleccionadas
    title_html = f'''
        <h3 align="center" style="font-size:20px"><b>Login Attempts from {start_time} to {end_time}</b></h3>
    '''
    m.get_root().html.add_child(folium.Element(title_html))

    # Guardar el mapa en html
    m.save('templates/map.html')
    print("Mapa creado: templates/map.html")

def main():
    data = read_json('login_attempts.json')

    # Recojo las fechas que se han escogido desde la webapp
    start_time = sys.argv[1]
    end_time = sys.argv[2]
    create_map(data, start_time, end_time)

if __name__ == "__main__":
    main()