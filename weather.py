import requests

API_KEY = "c09caadeebe8f770e1f84947a7ee8f09"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        # Build the request URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Check for errors
        if data.get("cod") != 200:
            print(f"Error: {data.get('message')}")
            return

        # Parse and display data
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"🌆 City: {city_name}\n🌡 Temperature: {temp}°C\n☁ Weather: {weather.capitalize()}")

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
