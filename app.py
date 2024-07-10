from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    # Formatear las fechas para que incluyan la hora 00:00:00
    start_time = f"{request.form['start_time']}T00:00:00Z"
    end_time = f"{request.form['end_time']}T00:00:00Z"
    
    obtener_datos = subprocess.run(
        ["python", "obtener_datos_api_jumpcloud.py", start_time, end_time],
        capture_output=True, text=True
    )
    print(obtener_datos.stdout)
    if obtener_datos.returncode == 0:
        crear_mapa = subprocess.run(["python", "crear_mapa_con_folium.py", start_time, end_time], capture_output=True, text=True)
        if crear_mapa.returncode == 0:
            return redirect(url_for('map'))
        else:
            return f"Error creating map: {crear_mapa.stderr}"
    else:
        return f"Error fetching data: {obtener_datos.stderr}"

@app.route('/map')
def map():
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)
