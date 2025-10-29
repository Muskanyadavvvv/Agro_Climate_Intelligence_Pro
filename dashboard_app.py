import streamlit as st
import pandas as pd
from fetch_weather_api import fetch_weather_data
from recommendation_chatbot import get_agri_recommendation
from map_visualization import app as show_yield_map
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="Agro Climate Intelligence Pro",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Agro Climate Intelligence Pro")
st.markdown("### AI-powered Climate & Crop Yield Forecasting System")

# Tabs
tabs = st.tabs(["📊 Overview", "🌦️ Weather & Forecast", "🗺️ Yield Map", "🧠 AI Recommendations"])

# --- Overview Tab ---
with tabs[0]:
    st.subheader("📈 Project Overview")
    st.markdown("""
    This AI-driven platform analyzes the impact of rainfall, temperature, and CO₂ emissions on crop yields.
    It integrates live climate data, hybrid AI models (Prophet + LSTM), and smart recommendations.
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/4276/4276926.png", width=250)
    st.success("Use the other tabs to explore live forecasts, maps, and AI-based insights.")

# --- Weather & Forecast Tab ---
with tabs[1]:
    st.subheader("🌦️ Real-Time Weather and Forecasting")

    city = st.text_input("Enter City Name", "Delhi")
    if st.button("Fetch Weather Data"):
        weather_data = fetch_weather_data(city)
        if weather_data:
            st.metric("🌡️ Temperature (°C)", f"{weather_data['temp']}")
            st.metric("💧 Humidity (%)", f"{weather_data['humidity']}")
            st.metric("☁️ Weather Condition", weather_data['description'])
        else:
            st.error("City not found or API error occurred.")

    st.markdown("---")
    st.info("📘 Future updates: Integration with Prophet + LSTM for yield forecasting coming soon.")

# --- Yield Map Tab ---
with tabs[2]:
    st.subheader("🗺️ Yield Forecast Visualization")
    show_yield_map()

# --- AI Recommendations Tab ---
with tabs[3]:
    st.subheader("🧠 Smart Agri Recommendation System")

    crop = st.selectbox("Select Crop", ["Rice", "Wheat", "Maize", "Sugarcane"])
    temp = st.slider("Average Temperature (°C)", 15.0, 40.0, 28.0)
    rain = st.slider("Annual Rainfall (mm)", 400.0, 1500.0, 900.0)
    yield_pred = st.slider("Predicted Yield (t/ha)", 1.0, 8.0, 4.5)

    if st.button("Generate Recommendation"):
        result = get_agri_recommendation(crop, temp, rain, yield_pred)
        st.success(result)




