# PhysComp SS23 Group 09 - Week 04

## Progress Report

### What we achieved this week

We created a first paper prototype in class using cardboards, hot glue and plastic cups. (Considering our first sketch and idea of the device). The device can hold a tablet with its triangular form and move its viewing angle with the two wheels. We did not include any buttons yet, because our initial sketch and idea didn't yet consider them really.  

#### First Physical Prototype

<img src="Figures/paperprototype.jpg" alt="Prototype" width="40%">

<img src="Figures/paperprototype_side.jpg" alt="Prototype Sideview" width="40%">

During the process, we had the idea of using 2 different colored LEDs to signal the user whether the device is currently connected. So we made some changes to the sketch and adapted the prototype a little. We chose indirect light from below the device so that it is both subtle but also able to immediately notify of a problem by changing the color.

#### Updated Sketch 

![Sketch Connection](Figures/SketchConnectionLight.jpg)

<img src="Figures/prototype_connected.jpg" alt="Prototype connected" width="40%">

<img src="Figures/prototype_notConnected.jpg" alt="Prototype notConnected" width="40%">

Initially, we considered incorporating a button or switch on the right side of our device to enable power on and off functionality. However, we eventually opted to design the device to automatically turn on once a tablet or smartphone gets placed into it and turn off as soon as it is removed. Here is a small sketch:

![Sketch PowerOn](Figures/SketchPowerOn.jpg)

Next, we also thought about the multimodality of our device and how we can process more physical input. We came up with the idea to give the user the possibility to switch between 3 different modes of operation:  

* Do nothing. Act as a tablet holder.
* Automatically rotate to follow the person's face that is currently in the video. Does nothing if multiple faces are in the video.
* Be remotely controlled by a participant who is not locally present. This requires the remote participant to log on to the device with a password.

These modes can be selected with the according button on the front bottom side of the device. A white LED (that is ideally built into the button) will signal the currently selected active mode.  

![Sketch Modi](Figures/SketchModi.jpg)

### Norman's Design Principles

1. Visibility:
   The triangular form and the slightly tilted board on the front of the device make it easy to understand that a phone/tablet has to be placed here. It resembles the shape of an ordinary book/tablet holder.
   The buttons for the 3 modes are also well visible. With descriptions above them, it should be obvious what they do.

2. Feedback:  
   The LEDs on the bottom give feedback of the current connection status and also signal whether the device is powered on. The LEDs in the front panel indicate the current operation mode.

3. Constraints: It is not possible to accidentally turn off the device (and therefore cut any connection) by pushing the wrong button. Likewise, it is not possible to turn off the device when removing the tablet, preserving battery life. Since tablets usually automatically rotate the image so that it is always correctly oriented, it is not even possible to place the tablet incorrectly into the device. Since the front panel buttons simply change the operation mode, it is not possible to do something wrong with them.

4. Mapping: 
   The buttons for the 3 different modes are all next to each other, well-labeled and at a reasonable position.  

5. Consistency:  
   The green light for connection and red light for no connection are consistent with the general understanding of those two colors. A little button on the front indicates that the respective mode is active.

6. Affordance: People are used to putting a book or tablet into a holder or are at least familiar with the concept. Also, people are used to the fact that things happen to the thing they interact with. In our case, the front panel button that is pressed will light up and the respective operation mode will be active. It would be unusual if a light somewhere else were to change. This is similar to our consistent mapping.

### Components List

* Raspberry Pi or Arduino if the RPi cannot be powered with batteries
* MicroSD card for the RPi
* Batteries (e.g. 9V) and power adapter
* Omni Wheel Base
* Three red and three green LEDs OR Three RGB LEDs or a strip
* Three Push-buttons with integrated white LEDs OR additional white LEDs
* A suitable switch that requires little force so that it can act as the main power switch
* Jumper wires
* Breadboard
* Resistors
* Wood or plastic pieces for the case and tablet holder
* Maybe 3D-printed parts

### What we could not achieve this week
We have not fully fleshed out the design of the button panel. Also, we have to find out about the capabilities of the omni wheel base that Matthias mentioned.

### What we plan to do for the coming week

We want to have a look at the omni wheel base from the class inventory. It might be a better solution for the mobility requirements of our device. Then, we can update the sketches and perhaps the paper prototype so they can be presented to the class.
