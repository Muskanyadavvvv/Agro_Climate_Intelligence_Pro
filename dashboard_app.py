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

# ---------- 🌍 APP HEADER ----------
st.title("🌾 Agro Climate Intelligence Pro")
st.markdown("""
#### A Smart Dashboard to Forecast, Analyze & Optimize Agricultural Productivity  
Empowered by AI • Driven by Data • Inspired by Nature 🌿
""")

st.markdown("---")

# ---------- 🌦️ Overview Metrics ----------
st.subheader("🌈 Quick Climate & Crop Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-card'>🌧️<br><b>Avg Rainfall</b><br>320 mm</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'>🌡️<br><b>Avg Temperature</b><br>28.4°C</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-card'>🌾<br><b>Avg Crop Yield</b><br>4.1 tons/ha</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------- 🧭 TABS FOR NAVIGATION ----------
tabs = st.tabs(["🌦️ Weather & Forecast", "🗺️ Yield Map", "🤖 AI Recommendations"])

# ---------- TAB 1: WEATHER ----------
with tabs[0]:
    st.markdown("<div class='tab-header'>🌦️ Real-Time Weather and Forecasting</div>", unsafe_allow_html=True)
    st.write("Enter your city to view the live weather and AI-based crop recommendations.")
    
    city = st.text_input("Enter City Name", "Delhi")
    if st.button("Fetch Weather Data"):
        try:
            weather_data = fetch_weather_data(city)
            st.success(f"Weather data for {city} fetched successfully!")

            # Display weather summary
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Temperature", f"{weather_data['temp']} °C")
                st.metric("Humidity", f"{weather_data['humidity']} %")
            with col2:
                st.metric("Wind Speed", f"{weather_data['wind_speed']} km/h")
                st.metric("Weather Condition", weather_data['description'].capitalize())

        except Exception as e:
            st.error(f"Error fetching data: {e}")

# ---------- TAB 2: YIELD MAP ----------
with tabs[1]:
    st.markdown("<div class='tab-header'>🗺️ Yield Forecast Visualization</div>", unsafe_allow_html=True)
    st.write("View yield forecast and rainfall impact across Indian states.")
    show_yield_map()

# ---------- TAB 3: AI RECOMMENDATIONS ----------
# --- AI Recommendations Tab ---
with tabs[2]:
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
<div class='footer'>
    © 2025 Agro Climate Intelligence Pro | Developed for B.Tech Final Year Project 🌾<br>
    <i>Empowering Sustainable Agriculture through AI, Data & Innovation.</i>
</div>
""", unsafe_allow_html=True)


