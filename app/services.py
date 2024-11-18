from datetime import datetime
from random import randrange, uniform
from app.config import Config
import requests


def get_random_sensor_data():
    return {
        "air_quality_index": randrange(0, 300),
        "date": datetime.now(),
        "water_quality_index": randrange(0, 100),
        "ph_level": round(uniform(0, 14), 2),
        "temperature": round(uniform(10, 100), 2),
    }


def get_weather_data():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    lat = 28.26689
    lon = 83.96851
    app_id = Config.OPEN_WEATHER_API_KEY
    url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={app_id}"
    res = requests.get(url).json()
    weather = {
        "feels_like": res["main"]["feels_like"],
        "humidity": res["main"]["humidity"],
        "temp": res["main"]["temp"],
        "temp_max": res["main"]["temp_max"],
        "temp_min": res["main"]["temp_min"],
        "description": res["weather"][0]["description"],
        "condition": res["weather"][0]["main"],
        "wind_deg": res["wind"]["deg"],
        "wind_speed": res["wind"]["speed"],
        "visibility":res["visibility"]
    }
    return weather
