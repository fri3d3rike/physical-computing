# PhysComp SS23 Group 09 - Week 08.md

## Soldering Exercise
Report on your soldering exercises (pictures/videos and text). What was your experience, what *challenges* did you face, what was the *outcome*?


### Challenges  

The main challege was to get the solder heated up at the right position, because not all sides of the soldering iron were hot. So it sometimes took a little patience or a new position of the soldering iron until the wire could be soldered. We used the helping hand and a flux pen, that helped the solder flow cleanly onto the parts we were soldering.
Another challenge was to reach the position between all the wires, but the helping hand and cutting and bending the finished wires away helped a lot and all in all we are satisfied with the result.
It took us some time to check the polarity of the components, but the manual and prints on the PCB told us everything we needed.

Here is a photo of us soldering: 

![MirzaSoldering](Figures/soldering-ex.jpg){width=40%}


### Outcomes 
Our outcome is a very nice littel light organ that lights up when the microphone detects a sound.

<table><tr>
<td> <img src="Figures/outcomeSoldering2.jpg" alt="Outcome1" style="max-width: 40%;"/> </td>
<td> <img src="Figures/outcomeSoldering1.jpg" alt="Outcome2" style="max-width: 40%;"/> </td>
</tr></table>


![](Figures/videoLEDOrgel.mp4)


## Weekly Progress Report

### What we achieved this week

Since the most important components have arrived, we wanted to start testing them to see if we need to order anything else. The powerbank and rolling lever switches work fine. The LED buttons however posed a little challenge. There was no data sheet and the Amazon website only stated something like "12V LEDs, switch 230V". Unfortunately, we found no other sellers that offered similar buttons with a more trustworthy description. We assumed the buttons the contain resistors to make them work with 12V. Just to be sure, we decided to test an orange button (a color we would not need later on) with 3.3V and quickly burned out the LED. We realized that the buttons do in fact not contain any resistors. We then soldered some of the left over leads from the soldering exercise to a new button and tested it on a breadboard with an appropriate 470 Ohms resistor. It worked just fine. This is nice because now we know that we won't need transistors to power the LED buttons.

![](Figures/button-legs.jpg){width=40%}

We also designed the CAD model for our front cover after measuring the buttons. Since the buttons are quite small, the panel has to be only 2 mm thin. We added ridges for structural stability. It is located in our concept folder and we would be happy to have it printed as soon as possible to see if everything fits.

<table><tr>
<td width="30%"> <img src="Figures/button-measure.jpg" alt="Outcome1"/> </td>
<td> <img src="Figures/frontpanel.png" alt="Outcome2"/> </td>
</tr></table>

### What we could not achieve this week

We have not reached our first milestone. We still have to create exact sketches or CAD models for the remaining structure of our device.

### What we plan to do for the next session (the coming week is a holiday)

* Decide which other parts must be 3D printed
* Create accurate sketches or CAD models
* Acquire the materials (cardboard, plastic)
