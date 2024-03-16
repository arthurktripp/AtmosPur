# AtmosPür Air Quality Monitoring
This is a project for Oregon State University's course, CS361 Software Engineering I.

## Description
This product allows the user to view and track the air quality in their home, while comparing it to the air quality outside.

From the home page, the user can easily view the current AQIs. The large font and dynamic colors communicate high level information at a glance. More information is also presented on this page, should a user need to read more.

The PürProgress feature tracks historic AQI daily averages, as well as the current day's minute-by-minute values. This is intended to give the user insight into how their home's air quality matches changes outside, especially when a nearby wildfire starts. Additionally, it informs the user how effective any changes they make can be: replacing or upgrading air filtration, investing in new windows or doors with better seals, etc.

## Implementation Notes
### Primary Application
At its core, AtmosPür is a Python Flask application. The app includes Jinja webpage rendering as well as API enpoints that support GET and POST requests. This serves as a central communication hub for several microservices.

### Home Monitoring
The inside device is prototyped with an MQ-2 sensor connected to an Arduino. The MQ-2 uses a semiconductor that has high electrical resistance in clean air, and lower resistance when in contact with different gasses and particles. A small electrical current is passed through the semiconductor, and any change in voltage is reflected in the analog output. 

A simple code loop in the Arduino measures this output, calibrates it to an estimated AQI value, and sends that to the computer via USB.

### Location-based AQI
A Location Service allows the user to update their home location, using a simplified search that employs a public API from OpenStreetMaps. That data is then saved in a static user settings JSON file that is accessed by another service that queries an API from the World Air Quality Index (waqi.info), which in turn provides data pulled from EPA. The application pulls new data once per second.

### Data Logging
Every minute, another service (coded by my OSU peer, Ben Kuhl) queries the main application for the indoor and outdoor AQIs. These are then logged into a JSON file for the current day. At midnight, these values are converted to an average for the day, and the current day's values are cleared. Another Flask application, this includes an endpoint that provides each tracked day's averages, as well as the current day's minute-by-minute updates.

### Historic Data Presentation
Using the ever-customizable graphing module, Bokeh, the service creates one of two line graphs that compare the indoor and outdoor AQIs over time. One displays the daily averages, while the other displays the minute-by-minute changes for the current day.

## Future Features
The user will be able to easily add additional air quality sensors throughout their house, probably via a WiFi mesh network. This would allow for granular monitoring in places that may require additional attention, such as bedrooms. 

It will also include a forecast of the upcoming three days.

Inside AQIs measurement needs to be calibrated.
