import random

def get_agri_recommendation(crop, temp, rain, yield_pred):
    recs = []
    if temp > 32:
        recs.append(f"⚠️ Temperature {temp}°C is too high for {crop}. Consider heat-resistant varieties.")
    elif temp < 20:
        recs.append(f"🌤️ Temperature {temp}°C is lower than ideal. Delay sowing for better results.")
    
    if rain < 700:
        recs.append("💧 Rainfall is insufficient. Irrigation or drought-tolerant crops recommended.")
    elif rain > 1200:
        recs.append("☔ Excess rainfall detected. Ensure proper field drainage.")
    
    if yield_pred > 5:
        recs.append("✅ Great yield potential! Maintain your current practices.")
    elif yield_pred < 3:
        recs.append("⚠️ Low yield forecast. Test soil and improve fertilization balance.")
    
    if not recs:
        recs.append("🌱 Conditions are favorable for cultivation.")

    return random.choice(recs)
