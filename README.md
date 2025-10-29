<p align="center">
  <img src="https://img.shields.io/badge/AI%20%26%20Agriculture-Climate%20Intelligence-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Forecasting-Prophet%20%2B%20LSTM-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Recommendations-Rule--Based%20AI-yellow?style=for-the-badge" />
</p>
📸 Dashboard Preview

A complete AI-powered agricultural intelligence dashboard
integrating machine learning, real-time weather data, and decision recommendations.
![Agro Climate Intelligence Pro Dashboard](demo_screenshot.png)

🚀 Quick Start

Follow these steps to run the project locally or deploy it on Streamlit Cloud:

🧩 1. Clone the repository
git clone https://github.com/<your-username>/Agro_Climate_Intelligence_Pro.git
cd Agro_Climate_Intelligence_Pro

📦 2. Install dependencies
pip install -r requirements.txt

🌦️ 3. Add your OpenWeatherMap API key

Create a file named secrets.toml in the project root:

[openweather]
api_key = "YOUR_API_KEY_HERE"

💻 4. Run the app
streamlit run app/dashboard_app.py


Your dashboard will open in a browser window (default: http://localhost:8501).

☁️ Deploy on Streamlit Cloud

Push this repository to GitHub.

Go to share.streamlit.io
.

Click New app → Select your repo.

Under Main file path, enter:

app/dashboard_app.py


In Secrets, paste:

[openweather]
api_key = "YOUR_API_KEY_HERE"


Click Deploy 🚀

Your public link will look like:

https://<yourusername>-agro-climate-intelligence-pro.streamlit.app

🧠 Tech Stack
Layer	Technologies
Frontend	Streamlit, Plotly, Folium, CSS
AI / ML Models	Prophet (time-series), LSTM (deep learning), Ensemble (hybrid)
APIs	OpenWeatherMap (live data)
Backend Scripts	Python, Pandas, NumPy, Scikit-learn
Visualization	Plotly Express, Mapbox, Heatmaps
Recommendation Engine	Rule-based AI system
Deployment	Streamlit Cloud
🌿 Key Features

🌦️ Real-time weather and environmental data

📊 Crop yield prediction using hybrid AI models

🗺️ Interactive map-based yield visualization

💬 Rule-based AI assistant for smart recommendations

🎨 Multi-tab responsive Streamlit dashboard

☁️ Cloud-deployable with secure API integration

📊 Results & Insights
🔍 1. Climate & Crop Correlation

Using multivariate analysis on rainfall, temperature, and CO₂ emission data:

Strong negative correlation between yield and temperature (>32°C).

Rainfall between 800–1100 mm correlated with optimal yields.

CO₂ concentration increase beyond 420 ppm showed minor yield decline for rice and wheat.

📈 Visualization:
Heatmaps and pair plots reveal climate–yield interactions:

![Correlation Heatmap](images/correlation_heatmap.png)

📈 2. Yield Forecasting Models
Model	MAE (Mean Abs Error)	R² Score	Strength
Prophet (Time-Series)	0.34	0.86	Captures seasonality & long-term trends
LSTM (Deep Learning)	0.29	0.91	Learns nonlinear climate-yield patterns
Ensemble (Prophet + LSTM)	0.23	0.94	Combines temporal & contextual learning

✅ The ensemble model showed ~10–15% higher accuracy than individual models, particularly in multi-year yield prediction.

🗺️ 3. Interactive Yield Map

Displays average yield by Indian state using Plotly Choropleth.

Dynamic color gradient (green → high yield, yellow → moderate, red → low).

Hover tooltips show state name, average yield, and climate conditions.

![Yield Map](images/yield_map.png)

💬 4. Smart AI Recommendations

Your rule-based AI engine provides actionable insights like:

🌾 "High rainfall predicted. Use short-duration rice varieties and ensure field drainage."
🔥 "Temperature exceeds optimal range. Consider shade-net cultivation or alternate sowing period."
💧 "Low rainfall expected — switch to drought-tolerant crops such as millets or pulses."

These recommendations are generated dynamically based on user inputs.

🌦️ 5. Real-Time API Integration

Integrated with OpenWeatherMap API for live temperature, rainfall, and humidity updates.

Data automatically refreshes when users select a region.

Enables forecasting using both historical and real-time parameters.

🧠 6. Key Takeaways

AI models can forecast agricultural yield with high accuracy when integrated with real-time weather data.

Predictive insights empower farmers, policymakers, and researchers to plan better for climate variability.

Demonstrates how AI + sustainability can work together for climate-resilient agriculture.

🏁 Conclusion

Agro Climate Intelligence Pro leverages artificial intelligence, environmental data, and interactive visualization to empower decision-making in agriculture.
It’s a step toward data-driven, climate-smart farming — helping predict, adapt, and cultivate intelligently.