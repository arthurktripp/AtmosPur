from bokeh.plotting import figure, show
from bokeh.resources import CDN, INLINE
from bokeh.embed import file_html, components
from bokeh.core.enums import SizingMode
from bokeh.layouts import column, row
from bokeh.models import RangeTool, ColumnDataSource
from datetime import datetime
import requests, json


def graph_aqi(graph_type="average"):
  response = requests.get('http://aqi.arthurktripp.com:5002/api')
  tracked_aqi = json.loads(response.text)
  date = []
  aqi_indoor = []
  aqi_outdoor = []
  
   
  if graph_type == "today":
    for each in tracked_aqi[-1][1]:
      date.append(datetime.strptime(each["Time"], "%I:%M %p"))
      aqi_indoor.append(each["Indoor AQI"])  
      aqi_outdoor.append(each["Outdoor AQI"])

    p = figure(title="Today's Details", 
              x_axis_label= "Time", 
              y_axis_label="AQI", 
              x_axis_type="datetime", 
              background_fill_color = "#d7d7d7FF", 
              border_fill_color = "#2A293400")
    p.line(date,
          aqi_indoor, 
          legend_label="Indoor AQI", 
          line_width=5, 
          color="#D36135FF", 
          line_join="bevel", 
          line_cap="round")
    p.line(date, 
          aqi_outdoor, 
          legend_label="Outdoor AQI", 
          line_width=5, 
          color="#2E599AFF",
          line_join="bevel",
          line_cap="round")
  else:
    for each in tracked_aqi:
      date.append(datetime.strptime(each[0], "%Y-%m-%d"))
      aqi_indoor.append(each[1][0]["Indoor AQI"])  
      aqi_outdoor.append(each[1][0]["Outdoor AQI"])
    
    p = figure(title="Daily Averages", 
              x_axis_label= "Date", 
              y_axis_label="AQI", 
              x_axis_type="datetime", 
              background_fill_color = "#d7d7d7FF", 
              border_fill_color = "#2A293400")
    p.line(date,
          aqi_indoor, 
          legend_label="Indoor AQI", 
          line_width=5, 
          color="#D36135FF", 
          line_join="bevel", 
          line_cap="round")
    p.line(date, 
          aqi_outdoor, 
          legend_label="Outdoor AQI", 
          line_width=5, 
          color="#2E599AFF",
          line_join="bevel",
          line_cap="round")


  p.title.text_color = "#D7D7D7FF"
  p.title.text_font = "Jost"
  p.title.text_font_size = "22px"
  
  p.xaxis.axis_label_text_color = "#D7D7D7FF"
  p.xaxis.axis_label_text_font = "Jost"
  p.xaxis.axis_label_text_font_style = "normal"
  p.xaxis.axis_label_text_font_size = "18px"
  p.xaxis.axis_line_color = "#D7D7D7FF"
  p.xaxis.major_label_text_color = "#D7D7D7FF"
  p.xaxis.major_tick_line_color = "#D7D7D7FF"
  p.xaxis.minor_tick_line_color = "#D7D7D7FF"
  
  p.yaxis.axis_label_text_color = "#D7D7D7FF"
  p.yaxis.axis_label_text_font_style = "normal"
  p.yaxis.axis_label_text_font = "Jost"
  p.yaxis.axis_label_text_font_size = "18px"
  p.yaxis.axis_line_color = "#D7D7D7FF"
  p.yaxis.major_label_text_color = "#D7D7D7FF"
  p.yaxis.major_tick_line_color = "#D7D7D7FF"
  p.yaxis.minor_tick_line_color = "#D7D7D7FF"
  
  p.outline_line_color = "#D7D7D7FF"
  p.grid.grid_line_color = "#BBBF"
  
  p.legend.background_fill_color = None
  p.legend.border_line_color = None

  # show(p)
  script, div = components(p)
  cdn_js = CDN.js_files[0]

  graph = {"script": script, "div": div, "cdn_js": cdn_js}
  return graph
  
  
if __name__ == "__main__":
  graph_aqi("today")
  