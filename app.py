from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "cb42b6b312dd441cb70170954250910" 

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    weather_bg = "/static/default.jpg" 

    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
        response = requests.get(url)
        data = response.json()

        
        if "error" not in data:
            weather_data = {
                "city": data["location"]["name"],
                "region": data["location"]["region"],
                "country": data["location"]["country"],
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "icon": "https:" + data["current"]["condition"]["icon"]
            }

            # 🌤 Choose background based on weather condition
            condition = weather_data["condition"].lower()
            if "sun" in condition or "clear" in condition:
                weather_bg = "/static/sunny.jpg"
            elif "rain" in condition or "drizzle" in condition or "shower" in condition:
                weather_bg = "/static/rainy.jpg"
            elif "cloud" in condition or "overcast" in condition:
                weather_bg = "/static/cloudy.jpg"
            elif "snow" in condition:
                weather_bg = "/static/snow.jpg"
            elif "storm" in condition or "thunder" in condition:
                weather_bg = "/static/storm.jpg"
        else:
            weather_data = {"error": data["error"]["message"]}

    return render_template('index.html', weather=weather_data, weather_bg=weather_bg)

if __name__ == '__main__':
    app.run(debug=True)
