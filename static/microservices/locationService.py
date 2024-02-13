import requests, json, time


def get_location():
    with open('./static/microservices/user-settings.json', 'r') as userSettings:
        userSettingsData = json.load(userSettings)
    return userSettingsData['location-search']
  

def get_loc_data():
    locationSearch = get_location()

    response = requests.get(f'https://nominatim.openstreetmap.org/search?q={locationSearch}&format=geojson')
    locationData = json.loads(response.text)
    loc_data = locationData["features"][0]

    return loc_data


def update_location():
    loc_data = get_loc_data()

    with open('./static/microservices/user-settings.json', 'r') as userSettings:
        userSettingsData = json.load(userSettings)

    displayName = loc_data['properties']['display_name']
    displayNameList = displayName.split(", ")
    name = loc_data['properties']['name']
    city = str(displayNameList[0])
    state = str(displayNameList[3])

    userSettingsData['location-name'] = name
    userSettingsData['home-location'] = city + ", " + state
    userSettingsData['home_lat'] = loc_data['geometry']['coordinates'][1]
    userSettingsData['home_long'] = loc_data['geometry']['coordinates'][0]

    with open('./static/microservices/user-settings.json', 'w') as userSettings:
        json.dump(userSettingsData, userSettings)
        

def listener():
  with open('./static/microservices/user-settings.json', 'r') as userSettings:
      userSettingsData = json.load(userSettings)
  location_search = userSettingsData['location-search']
  while True:
    time.sleep(.3)
    with open('./static/microservices/user-settings.json', 'r') as userSettings:
      userSettingsData = json.load(userSettings)
    location_check = userSettingsData['location-search']
    if location_search != location_check:
      update_location()
      with open('./static/microservices/user-settings.json', 'r') as userSettings:
        userSettingsData = json.load(userSettings)
      location_search = userSettingsData['location-search']

if __name__ == "__main__":
    listener()
    