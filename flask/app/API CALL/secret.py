import os

# Read API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

# Example endpoint: city name to coordinates

# http://api.openweathermap.org/geo/1.0/direct?q={Keonjhar}&limit=1&appid={OPENWEATHER_API_KEY}


# Example endpoint: coordinates to weather details

# http://api.openweathermap.org/data/2.5/weather?lat={21.6376203}&lon={85.6088638}&units=metric&appid={OPENWEATHER_API_KEY}
