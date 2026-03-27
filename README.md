#Weather CLI App

A Python command-line app that fetches real-time weather data for any city using the OpenWeatherMap API.

## Features
- Get live weather for any city in the world
- Shows temperature, humidity, wind speed and conditions
- Keeps running until you type 'quit'

## Tech Stack
- Python
- Requests library
- OpenWeatherMap API

## How to Run

1. Clone the repo
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app

2. Install dependencies
   pip install requests

3. Add your API key in weather.py
   API_KEY = "your_key_here"

4. Run the app
   python weather.py

## Sample Output

========================================
  Weather in London, GB
========================================
  Condition  : Clear sky
  Temperature: 15°C
  Feels like : 13°C
  Humidity   : 65%
  Wind speed : 3.2 m/s
========================================

## API Used
- [OpenWeatherMap](https://openweathermap.org/api)
