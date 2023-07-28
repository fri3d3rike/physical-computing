# PhysComp SS23 Group 09 - Week 15 - Final Report

## What we achieved in Week 14

As planned in our previous report, we added a third ultrasonic sensor in the back. This way, there is no risk of driving off an edge when going backward. There is no ultrasonic sensor in the front because we found nowhere to put it, it would look stupid and it also is not really necessary since you can see where you are going when driving forward.

![](Figures/all_back.jpg){width=40%}

The ultrasonic sensors on the sides are wired up and working. However, we don't trust them enough to test the edge detection when actually driving. Due to the weight of our device, the motors require a minimum power that makes it go quite fast. The measurements prove that it is indeed possible to detect an edge from the readings in theory.

![](Figures/ultra_console.png){width=40%}

Code by https://tutorials-raspberrypi.de/entfernung-messen-mit-ultraschallsensor-hc-sr04/

We also asked other students whether we should encase the ultrasonic sensors. The voted for yes with 2:1 votes. Our prototype now looks more polished:

![](Figures/ultra_exposed.jpg){width=40%}
![](Figures/ultra_encased.jpg){width=40%}

We decided that it isn't worth the effort to do more programming or even try to implement more functionality. Proper tracking would be nice, but also very time consuming to implement. We fixed a few bugs with the UI, though. In its current state, with a little bit of magic, our prototype can exactly showcase our whole vision for the telepresence system. This is why we call it complete and milestone 5 is reached (almost on time).

### We also found a missing photo of our drawing for the wooden parts

![](../Project/Concept/wood_drawing.jpg){width=20%}

We gave this drawing to the scientific engineering services. They cut our wood parts.

### Updated READMEs

We updated the READMEs of all directories in the Project directory to include useful information.

## Concluding report

Our prototype is a Telepresence Device designed for users attending hybrid meetings with their laptop or tablet. Its goal is to achieve a more active engagement in remote meetings. 

*what works*:
- Turning on the device with a switch by placing the tablet inside the holder
- Selecting between 3 different modes to change between different functionalities of the device 
- Giving the user feedback about which mode is currently selected by the according LED light, inside the button that was pressed, being turned on
- The device has red and green status LEDs underneath
- The device does not move when in mode: freeze
- The device moves in response to the remote participant pressing the keyboard or interacting with the graphical interface (and that pretty well and accurate)
- There is a graphical interface with which the remote participant can control the device
- The device has two out of three wired and working ultrasonic sensors to detect edges

*what plans changed*:
- We found a camera for the Raspberry Pi and then changed the concept to have a more independent device which does not also have to access the connected tablet/smartphone's camera
- We didn't fully implement the edge detection because we already planned in the beginning that that is not our main focus and we would only do it in the end, if we have enough time (optional goal)

*what doesn't work*:
- The tracking functionality (the OpenCV library caused problems)
- The feedback whether there is a connection to a remote (red/green status LEDs) user is not automatic yet (there is no login system)
- The edge detection: The ultrasonic sensors on the sides are wired up and working, only the one on the back is not wired. They do not force the device to stop yet, if an edge is detected. We did not implement it because we would not risk our device being damaged anyway.

*what could work if...*:
- All the things that are not completely functional yet could be improved to work if we would have had more time
- The ultrasonic sensors, as well as the feedback LEDs are connected to the raspberry pi, they just need to be implemented in the code to fully work (use the sensor readings which we already have, create some kind of session in JavaScript for the LEDs)
- The tracking would be a little bit more effort than the other things, but the camera is already connected and works and communicates with the pi, so we would need to get the library working. Then just send the appropriate motor commands if a face is detected far enough off-center.
- If the device were a bit lighter, than the motors could go slower (yes, its counter-intuitive). After the evaluation, we reduced the speed, but an even slower speed might be desirable.

### Demonstration

You can access our final presentation as [PDF](../Project/Concept/PhysComp_SS23_Final_Presentation.pdf) and [PPTX](../Project/Concept/PhysComp_SS23_Group_09_Final_Presentation.pptx) (with some videos included).

Here are some videos to show the prototype in action:

##### Setup 
![](Figures/Presentation/video-1.mp4)

##### Mode Selection
![](Figures/Presentation/video-2.mp4)

##### Remote Modus: UseCase 1
![](Figures/Presentation/video-3.mp4)

##### Tracking Modus: UseCase 2
![](Figures/Presentation/trackingMode.mov)

##### Edge Detection  
![](Figures/Presentation/edgeDetection.mov)

##### Device Rotating  
![](Figures/Presentation/rotatingDevice.mp4)
