# Buzzer

## Overview

Now we are going to make some noise!  We are going to use a simple Active Piezo Buzzer.  

This type of simple buzzers allow you to make annoying buzzing noises.

Here's a picture of what we are talking about.

##### Buzzer Top
![Buzzer Top](/images/buzzertop.jpg)  
##### Buzzer Bottom
![Buzzer Bottom](/images/buzzerbottom.jpg)


By simply adding power to them they make a sound.  You can take your buzzer and plug it directly into your power rail to hear it buzz.  They have a positve leg and a negative leg.  Just like an LED, the longer leg is the positive side and the negative side is the shorter leg. The buzzers in your kit are 3volt buzzers, so plug it into the top (3.3V) power rail, plugging the longer leg into the positive and the shorter leg to the negative.

Once it gets power, you should hear it's annoying buzz.

 ## What to do

In this lab, we are going to learn how to make the buzzer buzz at different frequencies with PWM.

In the last lab, we used PWM to fade an LED by updating the duty cycle after setting a fixed frequency.  With the buzzer, we will use the duty cycle to control the volume of the buzzer and use the frequency to control the pitch.

For wiring this one, we will remove the button from the last lab along with it's wires and then replace the LED with the buzzer.  You can plug the long leg (+) of the buzzer into Column 30 and the short leg(-) into Column 33.  Keep the wire going connecting the positive side of the buzzer at Column 30 to the Pico at column 20 (GP16).  Next run a wire from the short pin of the buzzer(-) to ground.  

![Buzzer Wiring Diagram](/images/11b_buzzer_bb.png)

Next we will write a simple program to fluctuate the PWM frequency to make our buzzer make sounds at different pitches.

Here is the code:

```Python
from machine import Pin, PWM
import utime

buzzer = PWM(Pin(16))


for freq in range(10, 1000, 100):
    buzzer.freq(freq)
    buzzer.duty_u16(30000)
    utime.sleep_ms(300)

```

This code will loop from 10 to 1000 with steps of 100. That is freq will be 10, then 110, then 210, then 310, etc... up to 1000.  This will cause the buzzer to buzz at each of these frequencies for 300 milliseconds(thanks to the sleep call) and at a hard coded duty cycle of 30000.  

If you got this to work, do your best bee impression and buzz!

## Stretch Goal

Play with the for loop the start and stopping range as well as the steps and the sleep time to get it to make interesting noises.  Rember with the `range(start, stop, step)` function, the start can be less than the stop if you use a negative step.  This way you can go backwards. 

Also, play with the duty cycle value passed to the `duty_u16()` method to see what impact that has.  Remember valid duty cycle values are between 0 and 65535 (max unsigned int size).


