import serial, time, requests, math


# check USB port with "python3 -m serial.tools.list_ports"
sensor = serial.Serial('/dev/cu.usbmodem143401', 9600, timeout=5)


def get_current_aqi():
  data_stream = str(sensor.readline())
  data_stream = data_stream[2:-3]
  signal = int(data_stream[0:-2])
  aqi = math.floor((signal / 10) ** 1.5)
  
  time_raw = time.localtime()
  time_log = time.asctime(time_raw)

  aqi_info = {"inside-aqi": aqi,
              "time": time_log}
  push_to_app(aqi_info)
  return


def push_to_app(aqi_data):
  response = requests.post("http://127.0.0.1:5001/api/inside", json=aqi_data)
  if response.status_code == 201:
    print('Message received by server')
  else:
    print('There was a problem: ', response.status_code)
  return
  

if __name__ == "__main__":
  while True:
    get_current_aqi()
    time.sleep(.3)