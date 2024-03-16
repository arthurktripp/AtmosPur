import requests, json, time


# use local coordinates to get the current local AQI
def get_aqi():
  lat_long = check_coords()
  latitude = lat_long[0]
  longitude = lat_long[1]
  
  response = requests.get(f'https://api.waqi.info/feed/geo:{latitude};{longitude}/?token=7d210291be3e69e61ccf8a33173c0263a65b0ded')
  aqiData = json.loads(response.text)
  aqiNum = aqiData["data"]["aqi"]
  aqiCity = aqiData["data"]["city"]["name"]

  print("The current AQI for", aqiCity, "is:", aqiNum)
  return aqiNum


# check the coordinates stored in the user settings json file
def check_coords():
  with open('./static/microservices/user-settings.json', 'r') as userSettings:
    userSettingsData = json.load(userSettings)
    lat_long = [userSettingsData['home_lat'], userSettingsData['home_long']]
  return lat_long


# posts the outdoor AQI to the main application
def send_local_aqi(data):
  time_raw = time.localtime()
  time_log = time.asctime(time_raw)
  aqi_json = {"outside-aqi": data,
              "time": time_log}
  url = "http://127.0.0.1:5001/api/outside"
  
  try:
    response = requests.post(url, json=aqi_json)
    if response.status_code == 201:
      print('Message received by server', response.status_code)
  except:
    print('There was a problem: ', response.status_code)
  return


if __name__ == "__main__":
  while True:
    local_aqi = get_aqi()
    send_local_aqi(local_aqi)
    time.sleep(1)
    
    