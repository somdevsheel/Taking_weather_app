import requests
import json
import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Get city name
city = input("Enter the city name: ")

# Weather API URL
url = f"https://api.weatherapi.com/v1/current.json?key=0d0d4aac8766427892a210525252501&q={city}"

try:
    # Make the API request
    r = requests.get(url)
    r.raise_for_status()  # Raise an error for HTTP issues

    # Parse the response
    weather_data = r.json()
    
    # Extract relevant data from response
    location = weather_data['location']
    current = weather_data['current']
    
    city_name = location['name']
    region = location['region']
    country = location['country']
    temp_c = current['temp_c']
    temp_f = current['temp_f']
    condition = current['condition']['text']
    wind_mph = current['wind_mph']
    wind_kph = current['wind_kph']
    wind_dir = current['wind_dir']
    pressure_mb = current['pressure_mb']
    humidity = current['humidity']
    feelslike_c = current['feelslike_c']
    feelslike_f = current['feelslike_f']
    visibility_km = current['vis_km']
    uv = current['uv']
    gust_mph = current['gust_mph']

    # Print detailed weather information
    print(f"Weather in {city_name}, {region}, {country}:")
    print(f"Temperature: {temp_c}°C ({temp_f}°F), Condition: {condition}")
    print(f"Feels like: {feelslike_c}°C ({feelslike_f}°F)")
    print(f"Wind: {wind_mph} mph ({wind_kph} kph), Direction: {wind_dir}")
    print(f"Pressure: {pressure_mb} mb, Humidity: {humidity}%")
    print(f"Visibility: {visibility_km} km, UV Index: {uv}")
    print(f"Wind Gusts: {gust_mph} mph")

    # Speak out each weather detail in smaller chunks
    engine.say(f"Weather in {city_name}, {region}, {country}:")
    engine.runAndWait()  # Allow time for the first sentence to finish
    engine.say(f"Temperature: {temp_c} degrees Celsius, {temp_f} degrees Fahrenheit.")
    engine.runAndWait()  # Allow time for the next sentence to finish
    engine.say(f"Condition: {condition}.")
    engine.runAndWait()
    engine.say(f"Feels like: {feelslike_c} degrees Celsius, {feelslike_f} degrees Fahrenheit.")
    engine.runAndWait()
    engine.say(f"Wind speed: {wind_mph} miles per hour, {wind_kph} kilometers per hour, from {wind_dir}.")
    engine.runAndWait()
    engine.say(f"Pressure: {pressure_mb} millibars, Humidity: {humidity}%.")
    engine.runAndWait()
    engine.say(f"Visibility: {visibility_km} kilometers. UV index: {uv}.")
    engine.runAndWait()
    engine.say(f"Wind gusts: {gust_mph} miles per hour.")
    engine.runAndWait()

except requests.exceptions.RequestException as e:
    print("Failed to fetch weather data. Please check your internet connection or API key.")
    engine.say("Failed to fetch weather data. Please try again later.")
    engine.runAndWait()
