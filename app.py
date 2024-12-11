# app.py
import streamlit as st
from fuzzy_logic import calculate_duration
from traffic_data import get_traffic_data, get_traffic_data_from_location
import os
import json
from dotenv import load_dotenv
import streamlit.components.v1 as components


# Ambil API key dari st.secrets
tomtom_api_key = st.secrets["tomtom"]["api_key"]
opencage_api_key = st.secrets["opencage"]["api_key"]

# Fungsi untuk mendapatkan lokasi dari IP
def get_ip_location():
    import requests
    url = "https://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()
    loc = data['loc'].split(',')
    latitude = loc[0]
    longitude = loc[1]
    return float(latitude), float(longitude)

# Fungsi untuk mendapatkan nama kota dan negara dari koordinat
def get_city_and_country(lat, lon):
    import requests
    url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={opencage_api_key}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        city = data['results'][0]['components'].get('city', 'Unknown City')
        country = data['results'][0]['components'].get('country', 'Unknown Country')
        return city, country
    else:
        return 'Unknown City', 'Unknown Country'

st.title("Durasi Lampu Lalu Lintas Dinamis dengan Fuzzy Logic")

option = st.radio("Pilih Metode", ["Otomatis (GPS)", "Manual (Database)"])

if option == "Otomatis (GPS)":
    # Ambil koordinat dari GPS
    lat, lon = get_ip_location()
    city, country = get_city_and_country(lat, lon)

    st.write(f"Lokasi: {city}, {country} (Latitude: {lat}, Longitude: {lon})")

    # Input
    num_people = st.slider("Jumlah Pejalan Kaki", 0, 100, 10)
    time_of_day = st.slider("Waktu (Jam)", 0, 23, 12)

    if st.button("Ambil Data Lalu Lintas (Otomatis)"):
        try:
            traffic_data = get_traffic_data(lat, lon)
            duration = calculate_duration(num_people, time_of_day)

            # Hasil
            st.write(f"Kecepatan Saat Ini: {traffic_data['speed']} km/h")
            st.write(f"**Kecepatan Normal**: {traffic_data['road_speed']} km/h")
            st.write(f"Tingkat Kepadatan: {traffic_data['occupancy']}")

            st.success(f"Durasi Lampu Hijau: {duration:.2f} detik")

            st.write("""
            **Note**:
            - **Kecepatan Saat Ini**: Kecepatan rata-rata kendaraan yang sedang bergerak di segmen jalan tersebut pada saat ini.
            - **Kecepatan Normal**: Kecepatan yang dianggap ideal jika lalu lintas lancar tanpa hambatan.
            - **Tingkat Kepadatan**: Nilai 1 menunjukkan kondisi sangat padat, dan 0 berarti jalan bebas hambatan.
            """)
            st.write("""
            **Data Sources**:
            Traffic data and congestion levels are sourced from the **TomTom Traffic API**, providing real-time traffic information.
            Location and city details are retrieved using the **OpenCage Geocoding API**, offering accurate geographical data based on coordinates.
            """)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

elif option == "Manual (Database)":
    # Baca data lokasi dari file locations.json (data update manual di locations.json)
    with open("locations.json", "r") as file:
        locations = json.load(file)

    # Pilih lokasi dari locations.json
    location_name = st.selectbox("Pilih Lokasi", list(locations.keys()))

    # Input untuk jumlah pejalan kaki dan waktu
    num_people = st.slider("Jumlah Pejalan Kaki", 0, 100, 10)
    time_of_day = st.slider("Waktu (Jam)", 0, 23, 12)

    if st.button("Ambil Data Lalu Lintas (Manual)"):
        try:
            # Ambil data lalu lintas dari lokasi yang dipilih
            traffic_data = get_traffic_data_from_location(location_name)

            # Perhitungan durasi lampu hijau berdasarkan jumlah pejalan kaki dan waktu
            duration = calculate_duration(num_people, time_of_day)

            # Menampilkan hasil
            st.write(f"Lokasi: {location_name}")
            st.write(f"Koordinat: Latitude {traffic_data['latitude']}, Longitude {traffic_data['longitude']}")
            st.write(f"Kecepatan Saat Ini: {traffic_data['speed']} km/h")
            st.write(f"Lebar Jalan: {traffic_data['road_width']} meter")
            st.success(f"Durasi Lampu Hijau: {duration:.2f} detik")

            # Catatan tambahan
            st.write("""
            **Note**:
            - **Kecepatan Saat Ini**: Kecepatan rata-rata kendaraan yang sedang bergerak di segmen jalan tersebut pada saat ini.
            - **Kecepatan Normal**: Kecepatan yang dianggap ideal jika lalu lintas lancar tanpa hambatan.
            - **Tingkat Kepadatan**: Nilai 1 menunjukkan kondisi sangat padat, dan 0 berarti jalan bebas hambatan.
            - **Lebar Jalan**: Lebar jalan berdasarkan data lokasi yang telah diatur.
            """)
            st.write("""
            **Data Sources**:
            Traffic data is sourced from the **TomTom Traffic API**. 
            Location information is predefined based on manual input or stored in a location dataset.
            """)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
