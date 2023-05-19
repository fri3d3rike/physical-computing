# PhysComp SS23 Group 09 - Week 06.md

## Feedback Report

### Concept Presentation

_Briefly summarize the feedback and comments you received on your concept presentation. List the most critical points (aim for at least 3)._

- Consider renaming the lables of the three front buttons on the device, because they might not be intuitive 
- Is the placement of the tablet on the device final? Maybe also consider the middle instead of the front for a better balance.
- How is the person/movement tracking implemented?

_Describe how you could address these (you’re welcome to discuss this hypothetically to achieve your vision, if you don’t plan to actually realizing it in your prototype)._

We thought about different names:
- off, disabled, still, hold, motionless, pause, freeze
- manual, remote
- automatic, track, follow

We then decided for two variants:
- Technical: disabled, auto, manual  
- Descriptive: freeze, follow, remote

We favor the descriptive terms because they are better understood by non-expert users.

The tracking is implemented solely with the tablet's camera. We do not use audio signals because we think that it is hard to locate their origin and to distinguish speaking from background noise. Also, we want to avoid the device moving around all the time because someone speaks.

![ButtonsSketch](Figures/buttonsSketch.jpg){width=30%}

### Peer Evaluation

_Briefly report on how you evaluated your own prototype/concept/story board with your partner group. (Did you discuss the story board? Did you play out a scenario in Wizard of Oz-style?) What was your experience?_

We used the storyboards to explain the possible functions and applications of our device and mostly worked with the paper prototype to disscuss improvements. Therefore it was really usefull to already have the low fidelity prototype to take it and imagine the final product. Not much of a simluation was needed because our features and use case are quite clear.

_What main feedback did you get here?_

### Feedback  
1. A way to change the angle of the smartphone/tablet would be helpful
2. Edge detection/feedback that the device is close to falling off the table is needed
3. Make the tablet more secured when it is on the device 
4. What happens when there is more than one person in front of the device (_follow mode_)?
5. Using a counter weight for a better balance 
6. Colors of the buttons?
7. A smartphone remote (app) would be cool

_What group did you partner up with for the prototype evaluation? Very briefly describe their project concept and summarize the most critical feedback points you gave them._

![Other Group](Figures/feedbackOthers.jpg){width=40%}

We partnered up with group 7. Their project is the Aurora Analog Timer. It's a time management tool for presentations consisting of two components. There is the main component, a timer with visual and sound feedback. The second component is a small remote with haptic feedback. You can also set checkpoints when you want to be reminded how much time you have left.

When giving our feedback we mostly had questions to the other team and ideas of what should also be considered. For example does the timer stop making a noise when the remote is placed back into the station on top of the main component or only if the stop button is pressed? What is the remote for? Could it maybe also be a laser pointer? Is there also a start and stop button on the remote? How is the checkpoint set? Can there be more than one checkpoint? Is there any feedback once the checkpoint is set? How can you add more time to the timer once it is already running? Is it possible to set more than 1h because that corresponds to one turn of the clock hand to set the time. Is there a maximum number of checkpoints? Is there a maximum time that can be set? Maybe it is smart to lable the inner circle with 15,30 and 45 minutes to indicate the time intervals. 


## Progress Report

_Update your concept/storyboard according to the feedback you received after your presentation and in the peer evaluation (you will need these illustrations again when you present your final project, so it’s worth the effort). Make sure you briefly report on these changes (in words/pictures)._

### Decisions regarding the Feedback we received

We think that the tablet won't fall off, but we will have to test this in practice once the motors are functional. We might limit the motor speed for slower acceleration/deceleration. We will have to test the final balance and maybe add a counter weight. We like our design with the tablet being right at the front of the device, minimizing the distance to the local participants.

The tracking is implemented solely with the tablet's camera. For simplicity, we decided that the device should not follow anyone if there are multiple people recognized in front of it. This way, the behavior should be easy to understand and predictable. 

In order to prevent the device from falling of edges, we might add ultrasonic sensors.

We have not fully decided on the button colors. In theory, the modes are equally relevant. Also, there are no intuitive colors for these modes. However, since the freeze mode should only be used temporarily (otherwise, you could just use a tablet stand), it might get a different color. In order to prevent a mapping like red = bad, the colors could be blue and white.

Regarding the smartphone remote, we are not sure if it is out of the scope of our project. We will keep it as an optional goal.

### What we achieved this week

We presented our concept to the class, got and gave feedback and then worked on improving our paper prototype and implemented the given feedback.  

We added something to change the angle of the tablet.  

![Prototype angles](Figures/prototype-2-angles.jpg)

And we renamed the three buttons and added descriptive icons. 

![Buttons updated](Figures/updatedButtons.jpg){width=70%}

![Prototype updated](Figures/prototype-2-updatedButtons.jpg){width=70%}

Also, we ordered the missing components so that we can try them next week and have time to order something else if needed. We ordered the following components from Amazon:

* Mikroschalter Rollenhebel 10 St. 4.99€
* LED Tastschalter 10 St. 7.99€
* Power Bank 20000mAh 21.95€

Links:
* https://www.amazon.de/dp/B07F9QKTQQ
* https://www.amazon.de/dp/B09QQJWTL5
* https://www.amazon.de/dp/B08G96F4ZF

### What we could not achieve this week

Nothing :)

### What we plan to do for the coming week

* Test the ordered components
* Create precise plans for building the device
* Think about parts that need to be 3D printed
* CAD modeling
* Maybe start soldering and building
