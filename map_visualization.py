import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def app():
    st.header("🗺️ Yield Forecast Visualization")

    try:
        # Load the sample dataset
        df = pd.read_csv("sample_agro_data.csv")

        # Add approximate latitude and longitude for each state (10 states)
        state_coords = {
            "Punjab": [31.1471, 75.3412],
            "Haryana": [29.0588, 76.0856],
            "Uttar Pradesh": [26.8467, 80.9462],
            "Madhya Pradesh": [23.4733, 77.9479],
            "Maharashtra": [19.7515, 75.7139],
            "Rajasthan": [27.0238, 74.2179],
            "Gujarat": [22.2587, 71.1924],
            "Bihar": [25.0961, 85.3131],
            "Tamil Nadu": [11.1271, 78.6569],
            "Karnataka": [15.3173, 75.7139]
        }

        # Map coordinates to dataframe
        df["Latitude"] = df["State"].map(lambda x: state_coords[x][0])
        df["Longitude"] = df["State"].map(lambda x: state_coords[x][1])

        # Create Folium map
        m = folium.Map(location=[22.5, 78.9], zoom_start=5, tiles="CartoDB positron")

        # Add markers for each state
        for i, row in df.iterrows():
            folium.CircleMarker(
                location=[row["Latitude"], row["Longitude"]],
                radius=7,
                color="green",
                fill=True,
                fill_color="yellow",
                popup=f"<b>{row['State']}</b><br>Crop: {row['Crop']}<br>Yield: {row['Yield']} tons/ha<br>Temp: {row['Temperature']}°C<br>Rainfall: {row['Rainfall']}mm"
            ).add_to(m)

        st_folium(m, width=725, height=500)

    except Exception as e:
        st.error(f"Error generating map: {e}")
