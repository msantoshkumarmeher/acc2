import os

import requests

# ============================================================
# API CALL - City to Coordinates to Weather
# File: city_to_coordinates.py
# Purpose: CLI script to fetch weather by city name using OpenWeather APIs
# ============================================================

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

def get_weather(city):
    try:
        if not API_KEY:
            print("Missing OPENWEATHER_API_KEY environment variable.")
            return

        # Step 1: Convert city name to latitude/longitude
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_data = requests.get(geo_url).json()

        if not geo_data:
            print("City not found!")
            return

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        # Step 2: Use coordinates to fetch weather details
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
        weather_data = requests.get(weather_url).json()


        # Step 3: Print formatted weather report in terminal
        print("\n--- Weather Report ---")
        print(f"City        : {city}")
        print(f"Condition   : {weather_data['weather'][0]['description']}")
        print(f"Temperature : {weather_data['main']['temp']} °C")
        print(f"Feels Like  : {weather_data['main']['feels_like']} °C")
        print(f"Humidity    : {weather_data['main']['humidity']}%")
        print(f"Wind Speed  : {weather_data['wind']['speed']} m/s")

    except Exception as e:
        print("Error:", e)


# Run script interactively
city = input("Enter city name: ")
get_weather(city)