from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "your_api_proj"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()
        if response.get("cod") == 200:
            weather_data = {
                "city": response["name"],
                "temp": response["main"]["temp"],
                "desc": response["weather"][0]["description"]
            }
        else:
            weather_data = {"error": response.get("message")}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
