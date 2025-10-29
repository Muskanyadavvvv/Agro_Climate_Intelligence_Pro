import random

def get_agri_recommendation(crop, temp, rain, yield_pred, soil_quality=None, humidity=None):
    recs = []

    # --- Temperature-based recommendations ---
    if temp > 34:
        recs.append(f"🔥 Temperature {temp}°C is too high for {crop}. Use shade nets or early morning irrigation to reduce heat stress.")
    elif temp < 20:
        recs.append(f"❄️ Temperature {temp}°C is below ideal for {crop}. Consider delayed sowing or protective covering at night.")
    else:
        recs.append(f"🌤 Temperature {temp}°C is suitable for {crop} growth.")

    # --- Rainfall-based recommendations ---
    if rain < 700:
        recs.append("💧 Rainfall is insufficient. Use drip irrigation or drought-tolerant crop varieties.")
    elif rain > 1200:
        recs.append("🌊 Excess rainfall detected. Improve drainage and avoid waterlogging.")
    else:
        recs.append("🌦 Rainfall is within an optimal range.")

    # --- Humidity-based recommendations ---
    if humidity is not None:
        if humidity > 80:
            recs.append("🌫 High humidity may increase fungal disease risk. Apply fungicides if necessary.")
        elif humidity < 40:
            recs.append("💨 Low humidity detected. Increase soil moisture retention using mulching.")

    # --- Soil Quality-based recommendations ---
    if soil_quality:
        if soil_quality.lower() in ["poor", "low"]:
            recs.append("🌱 Soil fertility is low. Add organic compost or NPK fertilizer mix.")
        elif soil_quality.lower() in ["medium"]:
            recs.append("🪴 Soil fertility is moderate. Maintain nutrient balance using urea and DAP in proportion.")
        elif soil_quality.lower() in ["good", "high"]:
            recs.append("🌾 Soil fertility is excellent. Maintain with crop rotation and green manure.")

    # --- Yield Prediction Insights ---
    if yield_pred > 5:
        recs.append(f"✅ Excellent yield potential for {crop}. Continue current practices and schedule timely harvesting.")
    elif yield_pred > 3:
        recs.append(f"🌿 Moderate yield potential for {crop}. Optimize watering and pest control.")
    else:
        recs.append(f"⚠️ Low yield forecast for {crop}. Perform soil testing and enhance fertilization management.")

    # --- Fertilizer Recommendations by Crop ---
    fertilizer_tips = {
        "wheat": "🧪 Apply 120kg N, 60kg P2O5, and 40kg K2O per hectare in split doses.",
        "rice": "💦 Maintain standing water; apply nitrogen in 3 equal splits.",
        "maize": "🌽 Use 150kg N and 75kg P2O5 per hectare; avoid excess urea.",
        "cotton": "🧤 Apply balanced nutrients with micronutrients like Zinc and Boron.",
        "soybean": "🌱 Use Rhizobium inoculation and phosphorus for better nodulation.",
    }

    if crop.lower() in fertilizer_tips:
        recs.append(fertilizer_tips[crop.lower()])

    # --- Final Random Encouraging Tip ---
    recs.append(random.choice([
        "🚜 Remember: Timely sowing increases yield by 10–15%.",
        "🌾 Rotate crops to improve soil fertility naturally.",
        "🌦 Schedule irrigation early morning or late evening for better absorption.",
        "🪴 Keep monitoring local weather forecasts for adaptive decisions."
    ]))

    return recs
