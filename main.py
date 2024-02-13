from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_socketio import SocketIO
import json, time


app = Flask(__name__)
app.config["SECRET_KEY"] = "password!"
socketio = SocketIO(app)

# location_service = subprocess.run(['python3', './static/microservices/locationService.py'], shell=True, capture_output=True, text=True)

inside_aqi = 0

def check_settings(key):
  userSettings = open("./static/microservices/user-settings.json", "r")
  userSettingsData = json.load(userSettings)
  return userSettingsData[key]
 

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "GET":
    location_search = check_settings("home-location")
    title = "AtmosPür"
    return render_template('index.html',
                          title = title,
                          inside_aqi = inside_aqi,
                          location_search = location_search)


@app.route("/location_search", methods=["POST"])
def location_search():
  if request.method == "POST":
    location_search = request.form['locationInput']
    with open('./static/microservices/user-settings.json', "r") as userSettings:
      userSettingsData = json.load(userSettings)

    if location_search != "":
      location_search += " USA"
      userSettingsData['location-search'] = location_search

    with open('./static/microservices/user-settings.json', "w") as userSettings:
      json.dump(userSettingsData, userSettings)

    print('New Location is: ', location_search)
    time.sleep(1)
    return redirect('/')



@app.route("/api/inside", methods=["POST"])
def post_listener():
  data = request.get_json()
  global inside_aqi
  inside_aqi = data['inside-aqi']
  return "AQI Updated", 201





if __name__ == "__main__":
  app.run(port=5001, debug = True)
  socketio.run(app)
