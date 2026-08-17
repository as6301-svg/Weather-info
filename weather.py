from dotenv import load_dotenv
import os
import json
import urllib.request as urlreq

load_dotenv()
API_KEY = os.getenv("API_KEY")

city = input("Enter city name: ")
try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = urlreq.urlopen(url)
    data = response.read()
    info = json.loads(data)
    print("Weather: ", info["weather"][0]["description"])
    print("Current Temperature: ", info["main"]["temp"], "Feels like: ", info["main"]["feels_like"])
    print("Humidity: ", info["main"]["humidity"])
    print("Wind Speed: ", info["wind"]["speed"])
except Exception as e:
    print("Error: ", e)