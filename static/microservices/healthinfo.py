import json

# return static information that cooresponds to current AQI
# uses health descriptions from EPA stored in a local JSON file
def getHealthData(aqi):
  with open("./static/health-info.json") as  data:
    healthdata = json.load(data)
    
    if (0 <= aqi <= 50):
      return healthdata["good"]
    elif (51 <= aqi <= 100):
      return healthdata["moderate"]
    elif (101 <= aqi <= 150):
      return healthdata["unhealthy-sensitive"]
    elif (151 <= aqi <= 200):
      return healthdata["unhealthy"]
    elif (201 <= aqi <= 300):
      return healthdata["very-unhealthy"]
    elif (301 <= aqi):
      return healthdata["hazardous"]
    