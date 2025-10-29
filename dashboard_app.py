import streamlit as st
import pandas as pd
import plotly.express as px
from fetch_weather_api import fetch_weather_data
from recommendation_chatbot import get_agri_recommendation as ai_recommendation
from map_visualization import app as show_yield_map

# ---------- 🌿 PAGE CONFIGURATION ----------
st.set_page_config(
    page_title="Agro Climate Intelligence Pro",
    page_icon="🌾",
    layout="wide"
)

# ---------- 🌈 CUSTOM STYLING ----------
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #d9fdd3, #e8f6ff);
            font-family: 'Segoe UI', sans-serif;
            color: #003300;
        }
        h1, h2, h3, h4 {
            color: #006400;
        }
        .metric-card {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 128, 0, 0.2);
            text-align: center;
            transition: transform 0.2s ease-in-out;
        }
        .metric-card:hover {
            transform: scale(1.05);
        }
        .tab-header {
            background-color: #d0f0c0;
            padding: 12px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            color: gray;
            margin-top: 50px;
            font-size: 13px;
        }
        .emoji {
            font-size: 22px;
            margin-right: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- 🌾 APP HEADER ----------
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #16a34a, #22c55e, #65a30d);
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.2);
        margin-bottom: 20px;">
        <h1 style="font-family:'Poppins',sans-serif; font-weight:700; margin:0;">
            🌿 Agro Climate Intelligence Pro
        </h1>
        <p style="font-size:18px; margin-top:5px;">
            A Smart Dashboard to Forecast, Analyze & Optimize Agricultural Productivity <br>
            <b>Empowered by AI • Driven by Data • Inspired by Nature 🌾</b>
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- 📊 OVERVIEW METRICS ----------
st.markdown("""
    <h2 style='text-align:center; color:#14532d; font-family:Poppins;'>
        🌈 Quick Climate & Crop Overview
    </h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div style="
            background-color:#ecfdf5;
            padding:20px;
            border-radius:15px;
            text-align:center;
            box-shadow:0 2px 5px rgba(0,0,0,0.1);">
            <h3>🌧️ Rainfall</h3>
            <p style="font-size:22px; color:#166534;"><b>320 mm</b></p>
            <p style="color:#4b5563;">Avg seasonal rainfall</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="
            background-color:#f0fdf4;
            padding:20px;
            border-radius:15px;
            text-align:center;
            box-shadow:0 2px 5px rgba(0,0,0,0.1);">
            <h3>🌡️ Temperature</h3>
            <p style="font-size:22px; color:#15803d;"><b>28.4°C</b></p>
            <p style="color:#4b5563;">Optimal range for major crops</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="
            background-color:#fefce8;
            padding:20px;
            border-radius:15px;
            text-align:center;
            box-shadow:0 2px 5px rgba(0,0,0,0.1);">
            <h3>🌾 Crop Yield</h3>
            <p style="font-size:22px; color:#b45309;"><b>4.1 tons/ha</b></p>
            <p style="color:#4b5563;">Predicted average yield</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------- 📂 TABS FOR NAVIGATION ----------
tabs = st.tabs([
    "🏠 Overview",
    "🌦️ Weather & Forecast",
    "🗺️ Yield Map",
    "🤖 AI Recommendations"
])

# ---------- TAB 1: WEATHER ----------
# ---------- 🌦️ WEATHER & FORECAST TAB ----------
with tabs[1]:
    st.markdown("""
        <div style="
            background: linear-gradient(90deg, #3b82f6, #06b6d4);
            padding: 15px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            margin-bottom: 25px;">
            <h2 style="font-family:Poppins; font-weight:700; margin:0;">
                🌦️ Real-Time Weather and Forecast
            </h2>
            <p style="font-size:16px;">Monitor temperature, humidity, rainfall & upcoming weather patterns</p>
        </div>
    """, unsafe_allow_html=True)

   # City Input Box
city = st.text_input("🏙️ Enter City Name", placeholder="e.g., Delhi")

if st.button("🔍 Fetch Weather Data"):
    if city:
        try:
            weather_data = fetch_weather_data(city)

            # --- Data Fallback (if API fails) ---
            if not weather_data:
                st.warning("⚠️ Unable to fetch live data. Showing default values for demo.")
                weather_data = {
                    "temperature": 28.0,
                    "humidity": 65,
                    "rainfall": 5,
                    "description": "Clear sky (Demo Mode)",
                    "wind_speed": 3.2,
                    "city": city
                }

            if weather_data:
                st.success(f"✅ Showing Weather Data for {city}")
                col1, col2, col3 = st.columns(3)
                # You can add display elements for temperature, humidity, etc. here

        except Exception as e:
            st.error(f"⚠️ Error fetching weather data: {e}")
    else:
        st.warning("⚠️ Please enter a city name.")


# ---------- TAB 2: YIELD MAP ----------
with tabs[2]:
    st.markdown("<div class='tab-header'>🗺️ Yield Forecast Visualization</div>", unsafe_allow_html=True)
    st.write("View yield forecast and rainfall impact across Indian states.")
    show_yield_map()

# ---------- TAB 3: AI RECOMMENDATIONS ----------
# --- AI Recommendations Tab ---
with tabs[3]:
    st.markdown("<h2 style='color:#16a34a; text-align:center;'>🌾 Smart AI Crop Recommendations</h2>", unsafe_allow_html=True)
    st.write("Our AI analyzes environmental data to provide actionable, data-driven recommendations for farmers.")

    # User Input Section
    with st.form("recommendation_form"):
        st.markdown("### 🌱 Enter Crop Parameters")

        col1, col2, col3 = st.columns(3)
        with col1:
            crop = st.text_input("Crop Name", "Wheat")
        with col2:
            temp = st.number_input("Average Temperature (°C)", 10.0, 50.0, 28.0)
        with col3:
            rain = st.number_input("Annual Rainfall (mm)", 100.0, 2000.0, 900.0)

        col4, col5 = st.columns(2)
        with col4:
            humidity = st.slider("Average Humidity (%)", 10, 100, 60)
        with col5:
            soil_quality = st.selectbox("Soil Fertility Level", ["Poor", "Medium", "Good"])

        yield_pred = st.slider("Predicted Yield (tons/hectare)", 1.0, 7.0, 4.0)

        submitted = st.form_submit_button("🔍 Get AI Recommendations")

    # Generate Recommendations
    if submitted:
        from recommendation_chatbot import get_agri_recommendation
        recs = get_agri_recommendation(crop, temp, rain, yield_pred, soil_quality, humidity)

        st.markdown("---")
        st.markdown("<h3 style='color:#0284c7;'>📋 Recommendations Summary</h3>", unsafe_allow_html=True)

        # Display results in colorful cards
        for r in recs:
            st.markdown(
                f"""
                <div style="
                    background-color:#f0fdf4;
                    border-left: 6px solid #16a34a;
                    padding: 12px;
                    margin: 10px 0;
                    border-radius: 10px;
                    box-shadow: 1px 1px 6px rgba(0,0,0,0.1);
                    font-size:16px;
                    color:#065f46;">
                    {r}
                </div>
                """,
                unsafe_allow_html=True
            )

        # Encouraging message
        st.success("🌿 AI Recommendations generated successfully! Implement these to optimize crop yield.")


# ---------- 🌱 FOOTER ----------
st.markdown("""
<div style='text-align:center; padding:20px; margin-top:40px; background-color:#f8f9fa; border-radius:12px;'>
    <h4 style='color:#2e8b57; margin-bottom:8px;'>Agro Climate Intelligence Pro</h4>
    <p style='color:#555; font-size:15px; margin:0;'>
        Empowering Sustainable Agriculture with <b>AI</b> and <b>Data Intelligence</b> 🌿
    </p>
    <p style='color:#888; font-size:13px; margin-top:6px;'>
        © 2025 Developed by <b>Muskan Yadav</b>
    </p>
</div>
""", unsafe_allow_html=True)









