import time
import os
import RPi.GPIO as GPIO
from pathlib import Path

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # main switch
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # remote
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # follow
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) # freeze
GPIO.setup(16, GPIO.OUT) # remote
GPIO.setup(20, GPIO.OUT) # follow
GPIO.setup(21, GPIO.OUT) # freeze

freeze = Path('freeze')
frozen = False
on = False

try:
  while True:
    main = not GPIO.input(4)
    if not main:
      GPIO.output(21, GPIO.LOW)
      GPIO.output(20, GPIO.LOW)
      GPIO.output(16, GPIO.LOW)
      if not frozen:
        freeze.touch()
      if on:
        os.system("~/off.sh")
      on = False
      continue
    elif not on:
      os.system("~/red.sh")
      GPIO.output(21, GPIO.HIGH)
      GPIO.output(20, GPIO.LOW)
      GPIO.output(16, GPIO.LOW)
      freeze.touch()
      frozen = True
      on = True
    if not GPIO.input(22):
      GPIO.output(21, GPIO.HIGH)
      GPIO.output(20, GPIO.LOW)
      GPIO.output(16, GPIO.LOW)
      freeze.touch()
      frozen = True
    if not GPIO.input(27):
      GPIO.output(21, GPIO.LOW)
      GPIO.output(20, GPIO.HIGH)
      GPIO.output(16, GPIO.LOW)
      freeze.unlink(missing_ok=True)
      frozen = False
    if not GPIO.input(17):
      GPIO.output(21, GPIO.LOW)
      GPIO.output(20, GPIO.LOW)
      GPIO.output(16, GPIO.HIGH)
      freeze.unlink(missing_ok=True)
      frozen = False
    time.sleep(0.01)
except KeyboardInterrupt:
  GPIO.cleanup()
