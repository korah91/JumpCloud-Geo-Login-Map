# JumpCloud-Geo-Login-Map
Python Flask tool for tracking all the login attempts to a JumpCloud Tenant in a map using JumpCloud's API. 
I made this cause I was bored and wanted to do something with JumpCloud. It was approximately 15 hours and is intended to showcase my skills in APIs and IAM

## Features
- Retrieve Login Attempts from the JumpCloud API.
- Geographical Visualization on an interactive map using [Folium Python library]([url](https://python-visualization.github.io/folium/latest/)).
- Custom Date Range: Adjust the date range to view specific login attempts. API Restriction of 90 day old logs
- Color-coded Markers: Differentiate between successful (green) and failed (red) login attempts with color-coded markers in the map.

## Requirements
- A JumpCloud tenant (obviously) with an admin account
- API Key of admin account in Jumpcloud
- requests, folium, flask and python-dotenv

## Project Structure
- app.py: Sets up Flask and orchestrates the data fetching and map creation process.
- obtener_datos_api_jumpcloud.py: Interacts with the JumpCloud API and retrieves login attempts
- crear_mapa_con_folium.py: Processes the data and generates an HTML map using Folium.
- templates: Folder for HTML templates for Flask
- .env: Configuration file for storing environment variables like the JumpCloud API key.


The tool works as expected, but maybe expect bugs :)

![Demostration](demo map login attempts.gif)

# Installation

Clone the repository:

    git clone https://github.com/korah91/JumpCloud-Geo-Login-Map.git
    cd JumpCloud-Geo-Login-Map

Create a .env file in the project's root directory and add your JumpCloud API Key:

    API_KEY=your_jumpcloud_api_key

Install dependencies:

    pip install -r requirements.txt

# Usage

Run the Flask application:

    python app.py

Open your browser and navigate to http://localhost:5000.

Adjust the start and end dates, then click "Run" to generate the map with login attempts.
