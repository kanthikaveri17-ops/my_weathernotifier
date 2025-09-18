from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "a2e7286c2062b7ee6faf1a4f70b094ad"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    try:
        res = requests.get(f"{BASE_URL}q={city}&appid={API_KEY}&units=metric").json()
        if res.get("cod") != 200:
            return None
        return {
            "city": city,
            "temp": res["main"]["temp"],
            "humidity": res["main"]["humidity"],
            "desc": res["weather"][0]["description"],
            "icon": res["weather"][0]["icon"]  # weather icon from API
        }
    except Exception as e:
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather = get_weather(city)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
  
