from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_socketio import SocketIO
import json, time
import healthinfo, makegraph

app = Flask(__name__)
app.config["SECRET_KEY"] = "password!"
socketio = SocketIO(app)

# location_service = subprocess.run(['python3', './static/microservices/locationService.py'], shell=True, capture_output=True, text=True)

inside_aqi = 0
outside_aqi = 0


def check_settings(key):
  userSettings = open("./static/microservices/user-settings.json", "r")
  userSettingsData = json.load(userSettings)
  return userSettingsData[key]
 

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "GET":
    insideData = healthinfo.getHealthData(inside_aqi)
    outsideData = healthinfo.getHealthData(outside_aqi)
    location_search = check_settings("home-location")
    location_name = check_settings("location-name")
    title = "AtmosPür"
        
    return render_template('index.html',
                          current_active = True,
                          title = title,
                          page_title = "Current Stats",
                          inside_aqi = inside_aqi,
                          outside_aqi = outside_aqi,
                          location_name = location_name,
                          location_search = location_search,
                          insideTitle = insideData["title"],
                          insideRange = insideData["range string"],
                          insideTagline = insideData["tagline"],
                          insideBody = insideData["body"],
                          outsideTitle = outsideData["title"],
                          outsideRange = outsideData["range string"],
                          outsideTagline = outsideData["tagline"],
                          outsideBody = outsideData["body"]                          
                          )


@app.route("/PurProgress", methods=["GET"])
def purprogress():
  if request.method == "GET":
    title = "PürProgress"
    location_search = check_settings("home-location")
    location_name = check_settings("location-name")
    graph_type = request.args.get('graph-type')
    graph = makegraph.graph_aqi(graph_type)
    
    return render_template('pur-progress.html',
                           purprogress_active = True,
                           title = title,
                           page_title = "PürProgress",
                           location_name = location_name,
                           location_search = location_search,
                           graph = graph)





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








# API ENDPOINTS:
@app.route("/api/inside", methods=["POST"])
def post_listener_inside():
  data = request.get_json()
  global inside_aqi
  inside_aqi = data['inside-aqi']
  return "AQI Updated", 201


@app.route("/api/outside", methods=["POST"])
def post_listener_outside():
  data = request.get_json()
  global outside_aqi
  outside_aqi = data['outside-aqi']
  return "AQI Updated", 201


@app.route("/api/data_tracking", methods=["GET"])
def send_data():
  time_raw = time.localtime()
  time_logged = time.asctime(time_raw)
  data = {"aqi_time": time_logged, "inside-aqi": inside_aqi, "outside-aqi": outside_aqi}
  
  return json.dumps(data)





if __name__ == "__main__":
  app.run(port=5001, debug = True)
  # socketio.run(app)


