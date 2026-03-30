import os

import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

def get_weather(city):
    try:
        if not API_KEY:
            print("Missing OPENWEATHER_API_KEY environment variable.")
            return

        # Step 1: Get coordinates
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_data = requests.get(geo_url).json()

        if not geo_data:
            print("City not found!")
            return

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        # Step 2: Get weather
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
        weather_data = requests.get(weather_url).json()


        # Step 3: Display result
        print("\n--- Weather Report ---")
        print(f"City        : {city}")
        print(f"Condition   : {weather_data['weather'][0]['description']}")
        print(f"Temperature : {weather_data['main']['temp']} °C")
        print(f"Feels Like  : {weather_data['main']['feels_like']} °C")
        print(f"Humidity    : {weather_data['main']['humidity']}%")
        print(f"Wind Speed  : {weather_data['wind']['speed']} m/s")

    except Exception as e:
        print("Error:", e)


# Run
city = input("Enter city name: ")
get_weather(city)