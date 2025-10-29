import requests
import streamlit as st

def fetch_weather_data(city):
    api_key = st.secrets["openweather"]["api_key"]
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200 and "main" in data:
            return {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "rainfall": data.get("rain", {}).get("1h", 0),
                "description": data["weather"][0]["description"].title(),
                "wind_speed": data["wind"]["speed"],
                "city": data["name"]
            }
        else:
            st.warning(f"⚠️ API Error: {data.get('message', 'Unknown error')}")
            return None

    except requests.exceptions.RequestException as e:
        st.error(f"Network Error: {e}")
        return None
