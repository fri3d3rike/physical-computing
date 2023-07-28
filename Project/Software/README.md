# Software

We wrote software to control the functionality of our prototype. There are two processors that we programmed:

* The Arduino Uno is for controlling the motors
* The Raspberry Pi is for handling user input and sending signals to the Arduino

## Arduino

The Arduino program is written in C and uses the Adafruit Motor Shield Library V2 to control the motors via the shield mounted onto the Arduino. It receives serial commands via USB from the Raspberry Pi. These commands contain (one byte each):

* Axis (forward/backward, left/right, rotate)
* Direction
* Motor speed

The program reads the commands in a loop and then sets the motor speeds accordingly.

https://github.com/adafruit/Adafruit_Motor_Shield_V2_Library

## Raspberry Pi

The Raspberry Pi is the brain of our prototype. Initially, we chose the Raspberry Pi because it is capable of image processing for the tracking mode. But since the actual tracking was not a top priority, we never actually implemented it. The main reason for that is that for some reason, the OpenCV library would not load the required modules. The Raspberry Pi handles all user input and sends commands to the Arduino. It provides the following functionality:

### A web server that serves our web UI

Since the Raspberry Pi has WiFi, we can connect it to a router and then access a small web server on it. The web server is realized in with Flask in Python. You can start it via ``start.sh``. It serves a static HTML page that has JavaScript code for GET requests when a button or key is pressed, found in ``static/index.html``. The GET requests are then handled by the Raspberry Pi. If the device is not in freeze mode, then the commands are forwarded to the Arduino to control the motors via serial commands. Since the hostname ``raspberrypi.local`` didn't work reliably (often quite delayed), we set up a static LAN address in the router.

Our code for the serial communication ``control.py`` was inspired by https://tutorials-raspberrypi.de/arduino-raspberry-pi-miteinander-kommunizieren-lassen/. We had to alter it to work with the current version of the library. 

### A Python script for our front panel

The ``frontpanel.py`` controls our front panel logic. It polls the buttons and sets the LEDs accordingly if a button is pressed. It also creates or removes the freeze file which indicates whether remote control has any effect. Since the "follow" mode is not implemented, it behaves the same as the "remote" mode, so we can simulate it.

### Some bash scripts for simulating functionality

The scripts ``red.sh``, ``green.sh`` and ``off.sh`` control the status LEDs below the device. Sine we have no actual login or connection system for the web UI, this simulates updating the status LEDs due to a user connecting/disconnecting.

### A python program for testing the ultrasonic sensors

The scripts ``ultra.py`` and ``ultra2.py`` poll fromt the left/right ultrasonic sensors. They show that the sensors are able to consistently detect edges. However, the data was never used because we did not want to risk our prototype breaking. Low motor speeds were not possible due to the weight, so the device was always a bit fast.

We took the electronic circuit and code from https://tutorials-raspberrypi.de/entfernung-messen-mit-ultraschallsensor-hc-sr04/ (modified).
