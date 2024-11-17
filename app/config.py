import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
