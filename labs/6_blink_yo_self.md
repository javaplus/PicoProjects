# Blink the Onboard LED

## Overview

We've finally made it to our first lab with actually using the Pico as a microcontroller and not as just a power source.  We will write our first bit of code in Python to have the Pico flash it's onboard LED!  This is the obligatory blink demo for nearly all microcontroller projects... this is the equivalent of the "hello world" program.

## Raspberry Pi Pico H

We are using the w1

 ## What to do

For this lab, we will replace the photoresistor in our circuit with our potentiometer.  So remove the photoresistor that connects the long side of the LED currently in column 30 to the power rail. 

Add the potentiometer to the breadboard making sure the side with the slots are near the middle section of the breadboard.  Make sure the 3 pins of the potentiometer are in different columns.  The far right pin when looking at the slots should go into the breadboard at Row G and column 25. This should position the middle pin into the breadboard at Row F and column 24.

With the potentiometer in place, connect the far left pin to our power rail. So, that should mean connecting a wire from the positive power rail to Column 23.  
Now connect the middle pin of the potentiometer which is in column 24 to the long leg of the LED in column 30.  Now connect the last pin (far right pin) of the potentiometer to ground.  That is run a wire from Column 25 to the ground(negative) rail.

If everything is connected properly you should be able to twist the knob ontop of the potentiometer and see the LED dim and brighten.  

If it works high five someone nearby.

![Resistor Circuit](/images/4_Circuit_bb.png)