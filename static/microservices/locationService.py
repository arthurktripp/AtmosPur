import requests, json, time


def get_location():
    with open('./static/microservices/user-settings.json', 'r') as userSettings:
        userSettingsData = json.load(userSettings)
    return userSettingsData['location-search']
  

def get_loc_data():
    locationSearch = get_location()

    response = requests.get(f'https://nominatim.openstreetmap.org/search?q={locationSearch}&format=geojson')
    locationData = json.loads(response.text)
    loc_data = locationData["features"][0]  # ["geometry"]["coordinates"]

    return loc_data


def update_location():
    loc_data = get_loc_data()

    with open('./static/microservices/user-settings.json', 'r') as userSettings:
        userSettingsData = json.load(userSettings)

    displayName = loc_data['properties']['display_name']
    displayNameList = displayName.split(", ")
    city = str(displayNameList[0])
    state = str(displayNameList[3])

    userSettingsData['home-location'] = city + ", " + state
    userSettingsData['home_lat'] = loc_data['geometry']['coordinates'][0]
    userSettingsData['home_long'] = loc_data['geometry']['coordinates'][1]

    with open('./static/microservices/user-settings.json', 'w') as userSettings:
        json.dump(userSettingsData, userSettings)


if __name__ == "__main__":
    update_location()
    
    