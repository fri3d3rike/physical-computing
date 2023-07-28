### Concluding report
To conclude your series of progress reports, please make a final post on Gitlab with the content outlined below.
As usually a lot of productive work happens in the very last week, this gives you the opportunity to highlight the updates and changes you made to your prototype for the demo.
You’re most welcome to just summarize/copy from your slides.

1. Briefly describe your final prototype (~2 lines, e.g., "Our prototype is xxx for yyy with zzz.").
Then remind us..

Our prototype is a Telepresence Device designed for users attending hybrid meetings with their laptop or tablet. Its goal is to achieve a more active engagement in remote meetings. 


*what works*:
- turning on the device with a switch by placing the tablet inside the holder
- selecting between 3 different modi to change between different functionalities of the device 
- giving the user feedback about which mode is currently selected by the according LED light, inside the button that was pressed, being turned on
- the device can give feedback whether there is a connection to a remote user or not
- the device does not move when in mode: freeze
- the device moves in response to the remote participant pressing the keyboard or interacting with the graphical interface (and that pretty well and accurate)
- there is a graphical interface with which the remote participant can control the device
- the device has two out of three wired and connected ultrasonic sensors to detect edges

*what plans changed*: if relevant, shortly describe any major deviation from your main concept (plan B?)
- we found a camera for the raspberry pi and then changed the concept to have a more independant device which does not also have to access the connected tablet/smartphone's camera
- we didn't fully implement the edge detection because we already planned in the beginning, that that is not our main focus and we would only do it in the end, if we have enough time

*what doesn't work*: outline in keywords what functionality your prototype is missing
- the tracking functionality
- the feedback whether there is a connection to a remote user is not automatic yet
- the edge detection: the ultrasonic sensors on the sides are wired up and working, only the one on the back is faked. Anyways they do not force the device to stop yet, if an edge is detected

*what could work if...*: reflect upon how future iterations could improve your prototype or what you would have done differently in retrospective
future:
- all the things that are not completly functional yet could be improved to work if we would have had more time
- the ultrasonic sensors, as well as the feedback LEDs are connected to the rasperry pi, they just need to be implemented in the code to fully work
- the tracking would be a little bit more effort than the other things, but the camera is already connected and works and communicates with the pi, so we would need to get the library working

2. In this post, include a video of your final prototype in action (e.g., the one from your slides). This is what will survive, even after your prototypes are take apart.

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



3. Ensure that all your source code, design files, etc. are in your GitLab repository. Please add a README.md file in the subfolder with your project code, listing libraries/tutorials/code sources that you used (including links). In particular, please point out files wherein the code was not implemented by you. Also, please describe how to build and run your code.