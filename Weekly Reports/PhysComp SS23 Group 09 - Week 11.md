# PhysComp SS23 Group 09 - Week 11

## Progress Report

### What we achieved this week

![Soldering](Figures/solderingButton.jpg){width=40%}

![Soldering](Figures/solderingButton2.jpg){width=40%}

We worked on Milestone 4. We soldered the buttons and connected them to the frontpanel. 

![Frontpanel](Figures/finishedFrontpanel.jpg){width=40%}

We assembled all the inner parts and started programming.

![innerParts](Figures/innerComponents_connected.jpg){width=40%}


![all Together](Figures/allTogether.jpg){width=40%}

In theory, the functions for moving in different directions are now ready, but we have not tested them.


We also created the Labels for the front panel:

![innerParts](Figures/frontpanelLabels.png){width=40%}

We created a letter of consent: [](../Project/Evaluation/consentletter.pdf)

We created two Google Forms for the pre and post test surveys and a consent form for our Evaluation Plan.


### Concept Change

Since we are using the Raspberry Pi camera for tracking participants, we no longer rely on a connection to the tablet. This makes our device more robust and makes the setup even easier. Now, the status LEDs no longer display the connection to the tablet, but
If the mode is freeze: whether the device is on
If the mode is follow: whether the device is detecting a participant to follow
If the mode is remote: whether a remote user is connected


### What we could not achieve this week

* Find people for the evaluation
* Milestone 4

### What we plan to do for the coming week

Finish milestone 4 and start with 5. 
* Front panel button labels
* Test driving
* Create web-interface for movement control
* Add status LEDs below the device
* Add on/off switch
* Write logic for controlling LEDs and on/off switch
* Assemble the rest (front panel, powerbank, tablet holder)
* Low priority: Mount Ultrasonic sensors and camera (not used for evaluation)

Find people for the evaluation of our prototype and evaluate.


## Evaluation Plan Refinement:

For the Evaluation Plan, the most remained the same as you can find in the last report of week 10.
We added the handout of a consent form in the introduction step of the procedure and also reworked the test tasks a little bit to be more specific.

### Introduction:
We greet the participant, introduce ourselves and briefly describe our project and the purpose of this study:
The purpose of this usability test is to evaluate the functionality, ease of use, and overall user experience of the telepresence device designed for users attending hybrid meetings as part of the Physical Computing Course SS23 at the University of Konstanz. The target group for this test is people who actively engage in remote meetings and need a seamless and immersive experience. The test will focus on assessing the device's rotation capabilities, tablet/phone holding mechanism, setup process, adaptability to different meeting spaces, and user interface.  
Then we give the participant a consent form to sign and introduce them to the tasks. 

### Test Tasks and Scenarios:

- Task 1: Device Setup:   
The user with the device is asked to unpack and set up the telepresence device on a table or desk. The user is provided with a tablet and asked to turn on the decive, by placing the tablet in the holder. Then both of the users are instructed to connect to the device.

While doing that we observe the user's experience during the setup process, noting any difficulties or confusion encountered.

- Task 2: Switch device into the Remote Mode:
The user with the device is asked to switch from the default mode of the device into the Remote Mode. Then the user is asked to check the conection status of the device.

- Task 3: Start Video Call:
The participants are asked to start a video call.

We observe how confident the user is with the use of their laptop. 

- Task 4: User Interface:
The useres are provided with a web-based interface for controlling the device.

We observe the user's interactions and note any challenges or areas of confusion. Do the two groups get the device to connected without problems?

- Task 5: Remote Control:
The remote user that is not present in the room with the device, is asked to rotate the device manually to look at different participants/directions in the other room. 

We observe if the device successfully rotates to track the user's face and adjusts its position accordingly. Drawing attention to excessive noise, delays, or inaccurate tracking.
 
- Task 6: Follow Mode selection and Rotating Functionality:
The users are asked to select a mode that causes the device to automatically follow a person in front of it. They are encouraged to move around. 

We observe if the device successfully rotates according to the users input and if the control via the keyboard was intuitive. 

- Task 8: Freeze Mode selection:
The users are instructed to set the mode, that stops the device from moving and prevents remote control. 

- Task 9: Turn off the device:
The user is asked to turn of the device by taking away the tablet.



## Milestone Review

No milestone is overdue. We would have liked more progress on milestone 4. We had to set the deadline quite late, but we need parts of the functionality for the evaluation. We will have to figure out how to handle this in the next session. We decided that it does not make sense to add another milestone specifically for the evaluation because it is hard to predict our progress.

1. Concept complete (DONE)
- Features clearly described
- Parts, sizes etc. planned out
- Mandatory and optional goals

2. All parts prepared (received, cut, printed) (DONE)
- Cutting
- Printing
- Ordering

3. Electronic components tested (DONE)
- Componentes tested individually
- Certain features tested: LEDs, buttons, camera, motors

4. Prototype assembled - Deadline 19.07.2023 (WIP)
- GOAL: Prototype assembled, components connected and tested
- TODO: Test driving code (weight/torque considerations)
- TODO: Properly mount ultrasonic sensors and camera
- TODO: Install LEDs under the device
- TODO: Mount front panel
- TODO: Mount powerbank
- TODO: Install on/off switch
- TODO: Finish tablet holder

5. Prototype functional - Deadline 26.07.2023
- GOAL: Programming complete
- TODO: On/off switch shows an effect
- TODO: Mode selection works
- TODO: Status LEDs work
- TODO: Remote control works
- OPTIONAL: Face tracking and automatic rotation
- OPTIONAL: Edge detection
