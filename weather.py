import requests

API_KEY = "2b65fc1c73c852a55cbeb109028b006e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {"q": city,"appid": API_KEY,"units": "metric"}
    response = requests.get(BASE_URL, params=params) 

    if response.status_code == 200:
        data = response.json()
        print("=" * 40)
        print(f"  Weather in {data['name']}, {data['sys']['country']}")
        print("=" * 40)
        print(f"  Condition  : {data['weather'][0]['description'].capitalize()}")
        print(f"  Temperature: {data['main']['temp']}°C")
        print(f"  Feels like : {data['main']['feels_like']}°C")
        print(f"  Humidity   : {data['main']['humidity']}%")
        print(f"  Wind speed : {data['wind']['speed']} m/s")
        print("=" * 40)
    else:
        print(f"City not found! Status code: {response.status_code}")


print("Weather App")
print("Type a city to get weather. Type 'quit' to exit.\n")

while True:
    city = input("Enter a city name: ").strip()
    if city.lower() == "quit":
        print("Goodbye!")
        break
    elif city:
        get_weather(city)
