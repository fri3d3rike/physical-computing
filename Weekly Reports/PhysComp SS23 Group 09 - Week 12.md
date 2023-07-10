# PhysComp SS23 Group 09 - Week 12

## Progress Report

### What we achieved this week

We made our prototype ready for the evaluation. Here is a list of what we have accomplished:

* Added front panel button labels
* Created web interface for remote-controlled driving
* We tested a direction connection to a laptop using a self-hosted WLAN hotspot
* The connection was too unstable, so instead we use a WLAN router for relaying the requests
* Tested the driving, found out that the batteries were too weak and replaced them
* Compensated a slow motor that caused the device to always turn by reducing the power of the other motors
* Added status LEDs below the device
* Added the on-off switch that is activated by placing the tablet into its slot
* Implemented logic for simulating the on-off switch (turns LEDs and functionality on/off)
* Implemented front panel logic (mode selection, corresponding LED is on, device ignores move commands if in freeze mode)
* Implemented a way to remote-control the status LEDs (red/green) below the device
* Glued on a power bank holder and the front panel

For photos, we refer to the evaluation.

We reached milestone 4 and part of milestone 5.

### What we could not achieve this week

We have not mounted the ultrasonic sensors and camera. This was not a problem because we had already planned to fake the edge detection and people recognition.

### What we plan to do for the coming week

* Mount the ultrasonic sensors and camera
* Incorporate some of the feedback from the evaluation: slower driving speed/acceleration, better web user interface
* Maybe more improvements if there is time
* Reach milestone 5
* Send refund requests for the components we bought

## Evaluation Report

### Participants

We recruited our six participants from students of other courses. For that, we asked them personally or wrote them texts on WhatsApp. Students are a good representation of our target group because after the pandemic, they are very familiar with video calls and the problems that can arise. We recruited them between the 4th and 7th of July 2023.

All participants signed letters of consent and aggreed on being recorded for our evaluation.

We had three groups of two participants each. One participant participated in the meeting in a room with Friederike using our device. The other participant went to a different room with Mirza.

### Functionality

The mode selection with LED feedback was actually working (except for the follow mode as mentioned before). In the freeze mode, no remote control is possible. Also, the remote-controlled driving was real since it is our core functionality.

We faked a lot of functionality. Since our web interface does not have a password-protected login system, remote users do not actually keep a connection to the device. They just send request whenever they issue a drive command. This is why Mirza simulated the connection status LEDs (red/green/off) by remotely running commands on his laptop at the correct times. We also faked the automatic following mode since it was not ready. Mirza remote-controlled the device from his laptop in this mode. We did not find a safe way to fake the edge detection, but we made sure that the situation would not arise by starting the experiment with the device in the middle of the table. This was important to protect the device from damage. We also faked the on-off switch. The effects were basically the same as if it were actually implemented (LEDs turn on/off, the device does not respond to commands when off, the device always starts in freeze mode). The only difference was that the power to the Arduino and Raspberry Pi was kept on, allowing us to always be able to intervene if something were to go wrong. Also, this was much easier to implement instead of actually hooking up all the components to the switch.

### Instructions

We changed some of the tasks to be more focused on the core concept and capabilities of our device.

- Task 0: Splitting up:
One user (local) stays with Friederike and the device. The other one (remote) goes to another room with Mirza.

- Task 1: Device Setup:   
The local user is provided with a tablet which is already in a Zoom call with Mirza's laptop next door. The remote participant can hear the instructions for the local participant through the call. The local participant is asked to turn on the decive by placing the tablet in the holder.

While doing that we observe the user's experience during the setup process, noting any difficulties or confusion encountered.

- Task 2: Switch Device into the Remote Mode:
The user with the device is asked to switch from the default mode of the device into the Remote Mode. Then the user is asked to check the conection status of the device (simuluated by Mirza).

- Task 3: Remote Control:
The remote user is asked to move the device manually to look at Friederike who sits outside of his field of view next to the local participant.

We observe if the device successfully moves and rotates toward Friederike. We check if it draws attention due to excessive noise, delays, or inaccurate movement.
We observe if the remote user can interact with the user interface. We instruct them to also try out the control via the arrow keys instead of the buttons.
 
- Task 4: Follow Mode Selection and Rotating Functionality:
The local user is asked to select a mode that causes the device to automatically follow a person in front of it. They are encouraged to move around so that the device has to rotate to keep them in the video.

We observe if the device successfully rotates according to the users input (simulated).

- Task 5: Freeze Mode selection:
The users are instructed to set a mode that stops the device from moving and prevents remote control. We encourage the remote user to attempt to move the device.

We observe if the mode selection is intuitive.

- Task 6: Turn off the device:
The local user is asked to turn of the device. If they do not know how, we give them the hint to take away the tablet.


### Observations

We made many interesting observations when watching the participants interact with our prototype.

* Although we explained the concept of our speak-aloud study, the participants generally kept quiet. We had to ask them to comment on their observations.
* If the tablet is in a protective case, some force is needed to push it into its place and activate the power switch. The first participant was not sure if they should apply so much force. For later trials, we remove the tablet case, making the process much simpler.
* One local user placed the tablet in portrait orientation instead of landscape orientation. We instructed them to change to landscape so that the tablet would not fall over.
* During one trial, a wheel came of. We were able to quickly stick it back onto its axle and continue the experiment.
* One participant acted as if they were afraid that the device could drive off the table.
* To one participant, it was not clear that the front panel LEDs are pushable buttons.
* During movement in one trial, the tablet briefly came off the switch, causing the device to quickly turn "off" and reset to the freeze mode. This was very unexpected and confused all of us.
* Some local participants did not notice the status LEDs below the device. We belief that this is because especially the red LEDs are not bright enough.
* In our web interface, users often did not use the "turn left"/"turn right" buttons, but instead only the "left" and "right" buttons. We should probably swap their places to make the more important rotation buttons more prominent. Likewise, the left/right arrow keys should control the rotation and only need "shift" for driving sideways. 

### Online Surveys

Both participants answered the same surveys. Some questions were more suitable for either the present or remote participant, but we always let both answer all questions from their perspectives. We evaluate them separately if appropriate.

#### Pre-Test Survey

![](Figures/Pretest/_How%20frequently%20do%20you%20participate%20in%20hybrid%20meetings%20or%20remote%20collaborations.png)

![](Figures/Pretest/_Which%20device%20do%20you%20usually%20use%20for%20remote%20meetings.png)

![](Figures/Pretest/_Please%20rate%20its%20effectiveness%20for%20your%20meetings.png)

![](Figures/Pretest/_How%20important%20is%20it%20for%20you%20to%20actively%20engage%20and%20contribute%20during%20remote%20meetings.png)

![](Figures/Pretest/_How%20familiar%20are%20you%20with%20telepresence%20devices%20or%20similar%20technologies_Please%20rate%20your%20familiarity.png)

![](Figures/Pretest/_How%20important%20is%20it%20for%20you%20to%20actively%20engage%20and%20contribute%20during%20remote%20meetings.png)

![](Figures/Pretest/_Have%20you%20used%20any%20rotating%20or%20tracking%20devices%20before_%20Please%20rate%20your%20experience%20with%20them.png)

![](Figures/Pretest/_How%20confident%20are%20you%20with%20using%20mobile%20apps%20or%20web-based%20interfaces%20for%20controlling%20physical%20devices_%20Please%20rate%20your%20level%20of%20confidence.png)

![](Figures/Pretest/_What%20features%20or%20functionalities%20do%20you%20expect%20from%20a%20telepresence%20device%20for%20hybrid%20meetings.png)


#### Post-Test Survey

### Post-Test Interview

After the experiment and the post-test survey, we briefly interviewed our participants together in person. We chose to do it this way to make it as comfortable as possible for them. We asked them especially for anything that they would like to comment on but did not write into the survey. We encouraged them to tell us everything about their experience during our study that came to their minds. Here are their comments:

* The device is quite loud
* They device might fall off the table
* The tablet camera angle is not ideal for large tables
* A way to remotely control the tablet angle vertically would help
* The device moves stuttery
* Unexpected movement scared someone
* The device is probably very good for presenters like professors
* A user placed the tablet in portrait orientation only because it already was this way on the table
* When asked, nobody noticed the possibility to manually change the vertical tablet angle
* A way to secure the tablet on the sides would be good
* Unsure what happens if there are many people in front of the device in automatic following mode
* The device is quite big and does not fit in a small bag, so it is not very portable
* Sometimes, the automatic tracking is too slow (was simulated to be as realistic as possible)
* Participants generally liked our front panel, the button labels, colors and feedback due to the LEDs lighting up
* At the beginning, it was not clear what the status LEDs below the device communicate (until they turned green exactly when the remote user "connected")

### Conclusions

We cannot make fundamental changes to our concept so shortly before the final presentation. For example, we cannot implement remote control for the vertical tablet angle. However, there are small things that we can polish:

* We can reduce the motor speed to make the device less scary, loud and abrupt
* We can make the acceleration gradual to make movements smoother
* We can swap the "turn" and sideways (left/right) buttons of our web interface
* We can add ultrasonic sensors for edge detection (or at least the simulation of it for our presentation)