from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.io import curdoc
from datetime import datetime
import requests, json


def graph_averages():
  response = requests.get('http://aqi.arthurktripp.com:5002/api')
  tracked_aqi = json.loads(response.text)
  date = []
  avg_indoor = []
  avg_outdoor = []
  for each in tracked_aqi:
    date.append(datetime.strptime(each[0], "%Y-%m-%d"))
    avg_indoor.append(each[1][0]["Indoor AQI"])  
    avg_outdoor.append(each[1][0]["Outdoor AQI"])  
  
  curdoc().theme = "dark_minimal"
  
  p = figure(title="Daily Averages", x_axis_label="Date", y_axis_label="AQI", x_axis_type="datetime")
  p.line(date, avg_indoor, legend_label="Indoor AQI", line_width=2, color="blue")
  p.line(date, avg_outdoor, legend_label="Outdoor AQI", line_width=2, color="red")

  show(p)
  return file_html(p, CDN, "my plot")
  

graph_averages()
