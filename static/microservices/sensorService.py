import serial, time, requests, math


# check USB port with "python3 -m serial.tools.list_ports"

ser = serial.Serial('/dev/cu.usbmodem144401', 9600, timeout=5)
url = "http://127.0.0.1:5001/api/inside"


def push_to_app(json_obj):
  response = requests.post(url, json=json_obj)
  if response.status_code == 201:
    print('Message received by server')
  else:
    print('There was a problem: ', response.status_code)
  return
  

def get_current_aqi():
  data_stream = str(ser.readline())
  data_stream = data_stream[2:-3]
  signal = int(data_stream[0:-2])
  aqi = math.floor((signal / 10) ** 1.5)
  
  time_raw = time.localtime()
  time_log = time.asctime(time_raw)
  print(aqi)
  aqi_json = {"inside-aqi": aqi,
              "time": time_log}
  
  push_to_app(aqi_json)
  return
  

if __name__ == "__main__":
  while True:
    get_current_aqi()
    time.sleep(.3)