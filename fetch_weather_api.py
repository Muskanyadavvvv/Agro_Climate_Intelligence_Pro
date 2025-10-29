import requests
import streamlit as st

def fetch_weather_data(city):
    api_key = st.secrets["openweather"]["api_key"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title()
        }
        return weather
    else:
        return None
