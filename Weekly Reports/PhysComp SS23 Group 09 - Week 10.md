# PhysComp SS23 Group 09 - Week 10

## Progress Report

### What we achieved this week
Friederike could not attend the lecture due to the overlap with another course, but worked from home. 
We got the wood parts we had ordered at the wood workshop and prepared them for the next milestone.

![Wood Parts](Figures/wood_parts.jpg){width=40%}

![Wood Component ](Figures/wood_component.jpg){width=40%}

We also managed to get the connection from the Raspberry Pi to the Arduino to work. We had to replace the camera cable to connect the camera to the Pi. For that, we borrowed a high quality camera module with a compatible cable. We do not use the high quality camera module, because it is very big and also requires a big lens which we do not have. With the new cable, out camera works, but for some reason the OpenCV library does not load certain modules on the Pi. We might implement the face tracking in a Wizard of Os fashion.

The first photo taken with the Raspberry Pi camera:

![First Pi Cam Image](Figures/picam.jpg){width=40%}

### What we could not achieve this week

The OpenCV library does not load the modules required for the face tracking. Also, the LEDs still have to be connected and the front panel must be assembled. The LED and motor controls have to be programmed.

### What we plan to do for the coming week

* Reach milestone 3
* Assemble everything (top part of the device, frontpanel, LEDs, camera, on-off switch)
* Setup the remote control

## Evaluation Plan:

### Usability Test Plan: Telepresence Device for Hybrid Meetings

### Introduction:
The purpose of this usability test is to evaluate the functionality, ease of use, and overall user experience of the telepresence device designed for users attending hybrid meetings. The target group for this test is people who actively engage in remote meetings and need a seamless and immersive experience. The test will focus on assessing the device's rotation capabilities, tablet/phone holding mechanism, setup process, adaptability to different meeting spaces, and user interface.

### Test Objectives:

- Evaluate the ease of setup and use of the telepresence device (turning it on).
- Evaluate the ease and understandability of the mode selection.
- Assess the functionality of the device's ability to rotate and its ability to follow a person's face.
- Determine the effectiveness and security of the tablet/phone holder.
- Test the adaptability of the device to different meeting spaces.
- Evaluate the intuitiveness and user-friendliness of the web-based interface of the remote participant.
- Gather feedback on overall user experience and identify areas for improvement.


### Number of Test Users:
To test the device we need at least pairs of two. So that one person can be with the physcial product while the other person interacts remotely (ideally from another room). If possible, it is preferable to have even multiple users interacting simultaneously during the test to simulate realistic meeting scenarios and assess any potential issues with concurrent usage. 


### Target Group: 
Users who regularly participate in hybrid meetings with their tablet/pc/smartphone etc. and requiring remote participation. The participants should have experience with remote collaboration tools and video conferencing software like Zoom, Teams, etc. Students are an ideal test group since they have experienced lots of video calls during the pandemic. They know the problems that they have had and can understand how they would benefit from our device.


### Test Tasks and Scenarios:

- Task 1: Device Setup:   
The user with the device is asked to unpack and set up the telepresence device on a table or desk. The user is provided with a tablet and asked to turn on the decive, by placing the tablet in the holder.

While doing that we observe the user's experience during the setup process, noting any difficulties or confusion encountered.

- Task 2: User Interface
The useres are provided with a web-based interface for controlling and connecting the device.
Then both of the users are instructed to connect to the device using the interface.

We observe the user's interactions and note any challenges or areas of confusion. Do the two groups get the device to connected without problems?

- Task 3: Remote Control:
The remote user that is not present in the room with the device, is asked to rotate the device manually to look at different participants in the other room. 

We observe if the device successfully rotates to track the user's face and adjusts its position accordingly. Drawing attention to excessive noise, delays, or inaccurate tracking.

- Task 4: Mode selection:
The users are instructed to set the mode to the freeze mode to prevent remote control. Then they are asked to select a mode that causes the device to automatically follow a persons in front of it.

- Task 5: Rotating Functionality:  
We instruct the user with the device to move around in the room while the device is set to follow their movements.  

We observe if the device successfully rotates according to the users input and if the control via the keyboard was intuitive. 


### Test Procedure:

1. Introduction and Pre-Test Survey:

Providing an overview of the test objectives and procedures to the participants. Asking for permission to collect the data and informing what the data is needed for. 
Collecting background information about the participants, including their experience with hybrid meetings and remote collaboration tools.

2. Demonstration:

We present a brief demonstration of the telepresence device's features and capabilities to familiarize participants with its functionality.

3. Test Execution:

We encourage the participants to think aloud, express their thoughts, and verbalize their experience as they use the device.
Assigning the tasks to the participant and taking notes on participants' interactions, difficulties and feedback.

4. Post-Test Survey:

Post-test questionnaire to gather additional feedback and subjective impressions from the participants.
Participants can ask questions, share their overall impressions, and provide any additional comments.

### Additional evaluation technique: Survey 

#### Pre-Test Survey: 

1. How frequently do you participate in hybrid meetings or remote collaborations? - [never, monthly, weekly, daily]

2. Which tools or devices do you currently use for remote meetings? Please rate their effectiveness on a scale of 1 to 5. [1 - Not effective, 5 - Highly effective]

3. On a scale of 1 to 5, how challenging do you find it to actively engage in remote meetings? [1 - Not challenging, 5 - Highly challenging]

4. How familiar are you with telepresence devices or similar technologies? Please rate your familiarity on a scale of 1 to 5. [1 - Not familiar, 5 - Very familiar]

5. On a scale of 1 to 5, how important is it for you to actively engage and contribute during remote meetings? [1 - Not important, 5 - Very important]

6. Have you used any rotating or tracking devices before? Please rate your experience with them on a scale of 1 to 5. [1 - Negative experience, 5 - Positive experience]

7. How confident are you with using mobile apps or web-based interfaces for controlling physical devices? Please rate your level of confidence on a scale of 1 to 5. [1 - Not confident, 5 - Very confident]

8. What features or functionalities do you expect from a telepresence device for hybrid meetings?

#### Post-Test Survey:

On a scale of 1 to 5... 

1. How would you rate the ease of setup and initial configuration of the telepresence device? [1 - Very difficult, 5 - Very easy]

2. Did you find the rotation functionality of the device effective in tracking your movements? [1 - Not effective, 5 - Highly effective]

3. Was the mode selection intuitive? [1 - Not intuitive, 5 - Very intuitive]

4. Did you feel that the telepresence device enhanced your ability to actively engage in the hybrid meeting? [1 - No impact, 5 - Significant impact]

5. On a scale of 1 to 5, how intuitive and user-friendly did you find the mobile app or web-based interface for controlling the device? [1 - Not intuitive, 5 - Highly intuitive]

6. How secure and stable did you find the tablet/phone holder for different sizes of devices?  [1 - Not stable, 5 - Highly stable]

7. How comfortable did you feel using the telepresence device during the test session? [1 - Not comfortable, 5 - Very comfortable]

8. Were there any challenges or difficulties you encountered when adapting the device to different meeting spaces?

9. What suggestions do you have for improving the overall usability and functionality of the telepresence device?

10. Based on your experience, would you consider using the telepresence device for your future hybrid meetings? Why or why not?


### What we hope to learn 

* What are common issues, patterns, and areas of improvement?
* Do people understand how to use the device (setup, mode selection)?
* What could be specified more clearly?
* How would we create a manual for the device?
* Are there any risks when using the device?

### What functionality can you test, what can you fake (Wizard of Oz)?

The changes in LED lights in response to button presses (mode selection, on/off switch, connectivity light) are hard to fake but easy to actually implement. We might have to simulate the device detecting edges via the ultrasonic sensors. Also, we might have to fake the mode of following a person if we cannot get the OpenCV library to work on the Pi.

![Gif](Figures/giphy1.gif)
