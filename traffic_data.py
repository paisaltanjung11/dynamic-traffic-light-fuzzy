#traffic_data.py
import os
import requests
import json
from dotenv import load_dotenv

# load API dari .env (secret)
load_dotenv()
API_KEY = os.getenv("TOMTOM_API_KEY")

# get data lalu lintas base coordinate (adj8) using tomtom
def get_traffic_data(lat, lon):
    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
    params = {
        "key": API_KEY,
        "point": f"{lat},{lon}"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "speed": data['flowSegmentData']['currentSpeed'],
            "road_speed": data['flowSegmentData']['freeFlowSpeed'],
            "occupancy": data['flowSegmentData']['confidence']
        }
    else:
        raise ValueError(f"API Error: {response.status_code} - {response.text}")

# get data lalu lintas dari lokasi (.json) manual
def get_traffic_data_from_location(location_name):
    with open("locations.json", "r") as file:
        locations = json.load(file)

    if location_name not in locations:
        raise ValueError(f"Lokasi '{location_name}' tidak ditemukan di locations.json")

    location = locations[location_name]
    lat, lon = location["latitude"], location["longitude"]

    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
    params = {
        "key": API_KEY,
        "point": f"{lat},{lon}"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "latitude": lat,
            "longitude": lon,
            "speed": data['flowSegmentData']['currentSpeed'],
            "road_width": location["road_width"]
        }
    else:
        raise ValueError(f"API Error: {response.status_code} - {response.text}")
