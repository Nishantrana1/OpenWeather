# weather_utils.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY") or "cb42b6b312dd441cb70170954250910"

def get_weather(city: str):
    """Fetch weather data for a given city using WeatherAPI."""
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return {"error": data["error"]["message"]}

    condition = data["current"]["condition"]["text"].lower()

    # Choose background and icon
    if "sun" in condition or "clear" in condition:
        bg = "static/sunny.jpg"
        icon = "static/sun.png"
    elif "rain" in condition or "drizzle" in condition or "shower" in condition:
        bg = "static/rainy.jpg"
        icon = "static/drizzle.png"
    elif "cloud" in condition or "overcast" in condition:
        bg = "static/cloudy.jpg"
        icon = "static/clouds.png"
    elif "snow" in condition:
        bg = "static/snow.jpg"
        icon = "static/snowflake.png"
    elif "storm" in condition or "thunder" in condition:
        bg = "static/storm.jpg"
        icon = "static/storm.png"
    elif "foggy" in condition or "mist" in condition:
        bg = "static/mist.jpg"
        icon = "static/mist.png"
    else:
        bg = "static/default.jpg"
        icon = "static/sun.png"
    
    return {
        "city": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "weather_bg": bg,
        "weather_icon": icon,
        "wind_kph": data["current"]["wind_kph"],
        "wind_dir": data["current"]["wind_dir"],
        "uv": data["current"]["uv"],
        "humidity": data["current"]["humidity"]
    }
