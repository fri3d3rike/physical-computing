import serial
import time
from flask import Flask
from flask import request
from os.path import exists

s = serial.Serial('/dev/ttyACM0', 115200)
def drive(axis, direction, speed):
  s.write(bytes([axis, direction, speed]))

app = Flask(__name__)

@app.route("/control")
def control():
    if exists("freeze"):
      return "frozen"
    axis = request.args.get("axis")
    direction = request.args.get("direction")
    speed = request.args.get("speed")
    drive(int(axis), int(direction), int(speed))
    return "ok: " + axis + ", " + direction + ", " + speed
