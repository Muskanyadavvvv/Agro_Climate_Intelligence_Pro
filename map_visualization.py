import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def app():
    st.header("🗺️ Yield Forecast Visualization")

    try:
        # Load dataset
        df = pd.read_csv("sample_agro_data.csv")

        # Approximate latitude and longitude for 10 Indian states
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

        # Map coordinates
        df["Latitude"] = df["State"].map(lambda x: state_coords[x][0])
        df["Longitude"] = df["State"].map(lambda x: state_coords[x][1])

        # Color scale based on yield
        def yield_color(y):
            if y >= 4.5:
                return "green"
            elif y >= 3.5:
                return "orange"
            else:
                return "red"

        # Create Folium map
        m = folium.Map(location=[22.5, 78.9], zoom_start=5, tiles="CartoDB positron")

        # Add circle markers
        for i, row in df.iterrows():
            popup_html = f"""
            <b>{row['State']}</b><br>
            Crop: {row['Crop']}<br>
            🌡️ Temp: {row['Temperature']}°C<br>
            🌧️ Rainfall: {row['Rainfall']} mm<br>
            🧪 CO₂: {row['CO2']} ppm<br>
            🌾 Yield: <b>{row['Yield']} tons/ha</b>
            """
            folium.CircleMarker(
                location=[row["Latitude"], row["Longitude"]],
                radius=10,
                color=yield_color(row["Yield"]),
                fill=True,
                fill_opacity=0.8,
                popup=folium.Popup(popup_html, max_width=250)
            ).add_to(m)

        # Add legend
        legend_html = """
        <div style="position: fixed; 
                    bottom: 50px; left: 50px; width: 180px; height: 120px; 
                    border:2px solid grey; z-index:9999; font-size:14px;
                    background-color:white; border-radius:8px;
                    padding: 10px 10px;">
        <b>Yield Levels</b><br>
        <i style="background:green;color:green;">....</i> High (≥4.5 tons/ha)<br>
        <i style="background:orange;color:orange;">....</i> Moderate (3.5–4.4)<br>
        <i style="background:red;color:red;">....</i> Low (<3.5)
        </div>
        """
        m.get_root().html.add_child(folium.Element(legend_html))

        st_folium(m, width=725, height=500)

    except Exception as e:
        st.error(f"Error generating map: {e}")
