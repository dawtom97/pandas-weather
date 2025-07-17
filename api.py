# z pliku config.py zaimportuj strukturę Settings (nazwa)
from config import Settings
import requests
import datetime
from tools import wind_speed, kelvin_to_celsius

def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Settings.city}&appid={Settings.api_key}"

    try:
        response = requests.get(URL)
        weather = response.json()

        data = {
            "Odczuwalna": kelvin_to_celsius(weather["main"]["feels_like"]),
            "Ciśnienie": weather["main"]["pressure"],
            "Wilgotność": weather["main"]["humidity"],
            "Zwykła temperatura": kelvin_to_celsius(weather["main"]["temp"]),
            "Opis pogody": weather["weather"][0]["description"],
            "Miejsce": weather["name"],
            "Prędkość wiatru": wind_speed(weather["wind"]["speed"]),
            "Data pomiaru": datetime.datetime.now()
        }
        return data

    except:
        print("Wystąpił błąd")
