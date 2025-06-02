import requests
api_key = "99659b12979751456bd7ae9ef3f45a9c"
lat = 38.674077
lon= -3.921077

weather_params = {
    "lat": 38.674077,
    "lon": -3.921077,
    "appid": api_key,
    "cnt" : 4,
}
answer = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
answer.raise_for_status()
weather_data = answer.json()

will_rain = False
for data in weather_data["list"]:
    condition_code = data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("take an umbrella")