import streamlit as st
import pandas as pd
import folium
import plotly.express as px
from streamlit_folium import st_folium

# Custom Streamlit Page Styling
st.markdown("""
    <style>
        /* Global app background */
        .stApp {
            background: linear-gradient(to bottom right, #f2fff2, #e6ffe6);
            color: #002b36;
            font-family: 'Segoe UI', sans-serif;
        }
        /* Header style */
        h1, h2, h3, h4 {
            color: #004d00 !important;
        }
        /* Card-like layout for each section */
        .stContainer {
            background-color: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 4px 15px rgba(0, 128, 0, 0.1);
            margin-bottom: 20px;
        }
        /* Legend Styling */
        .map-legend {
            background-color: white;
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 8px 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            font-size: 13px;
        }
        /* Subheader icons */
        .icon {
            font-size: 22px;
            margin-right: 6px;
        }
    </style>
""", unsafe_allow_html=True)

def app():
    st.markdown("<div class='stContainer'>", unsafe_allow_html=True)
    st.markdown("<h2>🗺️ Yield Forecast Visualization Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("<p>Explore state-wise agricultural performance using interactive maps and data insights.</p>", unsafe_allow_html=True)

    try:
        # Load dataset
        df = pd.read_csv("sample_agro_data.csv")

        # Coordinates for Indian states
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

        # Add coordinates
        df["Latitude"] = df["State"].map(lambda x: state_coords[x][0])
        df["Longitude"] = df["State"].map(lambda x: state_coords[x][1])

        # Define color scale
        def yield_color(y):
            if y >= 4.5:
                return "#2ecc71"  # green
            elif y >= 3.5:
                return "#f1c40f"  # yellow
            else:
                return "#e74c3c"  # red

        # --- Folium Map ---
        m = folium.Map(location=[22.5, 78.9], zoom_start=5, tiles="CartoDB positron")

        for i, row in df.iterrows():
            popup_html = f"""
            <b>{row['State']}</b><br>
            🌾 Crop: {row['Crop']}<br>
            🌡️ Temp: {row['Temperature']}°C<br>
            🌧️ Rainfall: {row['Rainfall']} mm<br>
            🧪 CO₂: {row['CO2']} ppm<br>
            <b>Yield:</b> {row['Yield']} tons/ha
            """
            folium.CircleMarker(
                location=[row["Latitude"], row["Longitude"]],
                radius=10,
                color=yield_color(row["Yield"]),
                fill=True,
                fill_opacity=0.8,
                popup=folium.Popup(popup_html, max_width=250)
            ).add_to(m)

        # Legend
        legend_html = """
        <div class='map-legend' style="position: fixed; bottom: 50px; left: 50px; z-index:9999;">
        <b>Yield Levels</b><br>
        <i style='background:#2ecc71;color:#2ecc71;'>....</i> High (≥4.5)<br>
        <i style='background:#f1c40f;color:#f1c40f;'>....</i> Moderate (3.5–4.4)<br>
        <i style='background:#e74c3c;color:#e74c3c;'>....</i> Low (<3.5)
        </div>
        """
        m.get_root().html.add_child(folium.Element(legend_html))

        # Display Map
        st_folium(m, width=725, height=500)

        st.markdown("</div>", unsafe_allow_html=True)

        # --- Chart Section ---
        st.markdown("<div class='stContainer'>", unsafe_allow_html=True)
        st.markdown("<h3>📊 Yield vs Rainfall Analysis</h3>", unsafe_allow_html=True)
        st.markdown("<p>This chart visualizes how rainfall impacts crop yield across different states.</p>", unsafe_allow_html=True)

        fig = px.scatter(
            df,
            x="Rainfall",
            y="Yield",
            color="State",
            size="Temperature",
            hover_name="Crop",
            trendline="ols",
            labels={"Rainfall": "Rainfall (mm)", "Yield": "Yield (tons/ha)"},
            title="Relationship between Rainfall and Crop Yield"
        )
        fig.update_layout(
            title_font=dict(size=18, color="#004d00"),
            paper_bgcolor="white",
            plot_bgcolor="#f9fff9",
            font=dict(family="Segoe UI", color="#003300")
        )
        fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error generating map: {e}")
