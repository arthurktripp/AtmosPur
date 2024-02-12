import requests
import json

global homeLocation

def location_check():
  with open('user-settings.json', 'r') as userSettings:
    userSettingsData = json.load(userSettings)
  
  homeLocation = userSettingsData['home-location']


response = requests.get('https://api.waqi.info/feed/here/?token=7d210291be3e69e61ccf8a33173c0263a65b0ded')
aqiData = json.loads(response.text)
aqiNum = aqiData["data"]["aqi"]
aqiCity = aqiData["data"]["city"]["name"]

print("The current AQI for", aqiCity, "is:", aqiNum)


def check_aqi():
  return