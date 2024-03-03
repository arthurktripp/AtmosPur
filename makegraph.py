from bokeh.plotting import figure, show
from bokeh.resources import CDN, INLINE
from bokeh.embed import file_html, components
from bokeh.core.enums import SizingMode
from bokeh.layouts import column, row
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
  p.line(date, avg_indoor, legend_label="Indoor AQI", line_width=5, color="#2E599AFF", line_join="bevel", line_cap="round")
  p.line(date, avg_outdoor, legend_label="Outdoor AQI", line_width=5, color="#2E599AFF",  line_join="bevel", line_cap="round")
  p.background_fill_color = "#d7d7d7ff"
  
  layout = column()
  layout.sizing_mode = "stretch_both"

  # show(p)
  script, div = components(p)
  cdn_js = CDN.js_files[0]
  
  graph = {"script": script, "div": div, "cdn_js": cdn_js}
  return graph
  
  
if __name__ == "__main__":
  graph_averages()
