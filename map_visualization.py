import pandas as pd
import plotly.express as px
import streamlit as st
import requests
import json

def show_yield_map(data_path="sample_agro_data.csv"):
    try:
        df = pd.read_csv(data_path)
        df["State"] = ["Uttar Pradesh", "Punjab", "Maharashtra", "Bihar", "Tamil Nadu", "Gujarat"] * (len(df)//6 + 1)
        df = df.head(len(df))
        state_yield = df.groupby("State")["Yield(t/ha)"].mean().reset_index()

        # India geojson
        india_url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson"
        geojson_data = json.loads(requests.get(india_url).text)

        fig = px.choropleth(
            state_yield,
            geojson=geojson_data,
            featureidkey="properties.NAME_1",
            locations="State",
            color="Yield(t/ha)",
            color_continuous_scale="YlGn",
            title="Predicted Average Yield per State (t/ha)",
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error generating map: {e}")

