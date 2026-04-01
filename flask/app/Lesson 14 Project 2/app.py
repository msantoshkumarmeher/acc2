from flask import Flask, render_template, request
import json
import os
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# ============================================================
# Lesson 14 - Weather App Project
# File: app.py
# Purpose: Fetch city weather from OpenWeather API and show in UI
# ============================================================

app = Flask(__name__)

# Read the OpenWeather key from the environment for safe publishing.
API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"
GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"
CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_coordinates(city):
    # Step 1: Convert city name to latitude/longitude using geocoding API
    params = {
        "q": city,
        "limit": 1,
        "appid": API_KEY,
    }
    url = f"{GEO_URL}?{urlencode(params)}"

    with urlopen(url, timeout=10) as response:
        payload = response.read().decode("utf-8")
        results = json.loads(payload)

    if not results:
        raise ValueError("City not found")

    first_match = results[0]
    return first_match["lat"], first_match["lon"], first_match.get("name", city)


def fetch_weather(lat, lon, units="metric"):
    # Step 2A: Try One Call API for richer weather data
    params = {
        "lat": lat,
        "lon": lon,
        "exclude": "minutely,hourly,alerts",
        "units": units,
        "appid": API_KEY,
    }
    url = f"{BASE_URL}?{urlencode(params)}"

    with urlopen(url, timeout=10) as response:
        payload = response.read().decode("utf-8")
        return json.loads(payload)


def fetch_current_weather(city, units="metric"):
    # Step 2B: Fallback API (current weather only)
    params = {
        "q": city,
        "units": units,
        "appid": API_KEY,
    }
    url = f"{CURRENT_URL}?{urlencode(params)}"

    with urlopen(url, timeout=10) as response:
        payload = response.read().decode("utf-8")
        return json.loads(payload)


@app.route("/", methods=["GET", "POST"])
def home():
    # Variables passed to template (default state)
    weather = None
    error = None
    city = ""
    units = "metric"

    if request.method == "POST":
        # Read form values
        city = request.form.get("city", "").strip()
        units = request.form.get("units", "metric").strip() or "metric"

        try:
            if not API_KEY:
                # API key must be set in environment variable
                raise ValueError("Missing OPENWEATHER_API_KEY environment variable.")

            if not city:
                raise ValueError("Please enter a city name.")

            if units not in {"metric", "imperial", "standard"}:
                units = "metric"

            lat, lon, resolved_city = fetch_coordinates(city)

            try:
                # Primary call (One Call API)
                data = fetch_weather(lat, lon, units)
                current = data.get("current", {})
                daily = data.get("daily", [])
                today = daily[0] if daily else {}

                weather = {
                    "city": resolved_city,
                    "timezone": data.get("timezone", "N/A"),
                    "temp": current.get("temp", "N/A"),
                    "feels_like": current.get("feels_like", "N/A"),
                    "humidity": current.get("humidity", "N/A"),
                    "wind_speed": current.get("wind_speed", "N/A"),
                    "description": (
                        current.get("weather", [{}])[0].get("description", "N/A").title()
                    ),
                    "today_min": today.get("temp", {}).get("min", "N/A"),
                    "today_max": today.get("temp", {}).get("max", "N/A"),
                }
            except HTTPError as onecall_err:
                # One Call 3.0 often requires a paid plan; fallback keeps app usable.
                if onecall_err.code != 401:
                    raise

                # Fallback to current weather endpoint
                data = fetch_current_weather(resolved_city, units)
                main = data.get("main", {})
                wind = data.get("wind", {})

                weather = {
                    "city": data.get("name", resolved_city),
                    "timezone": "Local City Time",
                    "temp": main.get("temp", "N/A"),
                    "feels_like": main.get("feels_like", "N/A"),
                    "humidity": main.get("humidity", "N/A"),
                    "wind_speed": wind.get("speed", "N/A"),
                    "description": (
                        data.get("weather", [{}])[0].get("description", "N/A").title()
                    ),
                    "today_min": main.get("temp_min", "N/A"),
                    "today_max": main.get("temp_max", "N/A"),
                }
        except ValueError as value_err:
            if str(value_err) == "City not found":
                error = "City not found. Please enter a valid city name."
            else:
                error = str(value_err)
        except HTTPError as http_err:
            if http_err.code == 401:
                error = "Invalid API key. Please check your OpenWeather API key."
            elif http_err.code == 400:
                error = "Bad request. Please verify city name and try again."
            else:
                error = f"OpenWeather API error: HTTP {http_err.code}."
        except URLError:
            error = "Network error. Please check your internet connection."
        except Exception:
            error = "Something went wrong while fetching weather data."

    return render_template(
        "index.html",
        weather=weather,
        error=error,
        city=city,
        units=units,
    )


if __name__ == "__main__":
    app.run()
