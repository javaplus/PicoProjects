# FIRE ZEE LASERS!!!!1!!

## Overview

You are now well prepared for our final objective.  What's a mad scientist pre-compiler without a little fun with lasers and target practice??

In this part 1 of 3 for our final game you will do the following:

- Wire the photo resistor through the two little holes in the middle of your target and place the target end cap on one end of the ruler with the photo resistor side facing towards the rest of the ruler
- Detect a button press (use various button labs as a reference)... if this happens the pico should FIRE ZEE LASER at the photoresistor (our target).
- You then need to read the current value of the photoresistor to see if you scored a "hit", that is did the value of the photoresistor change dramatically when the laser was shining on it.
- Once the button has been pressed we need to lock out the player from another attempt for 5 seconds (use debounce lab as a reference)

  
 ## What to do

### Build the Target:

Put the photo resistor legs through the two holes in the center of the target.  The legs should come out the back flat side of the target. On the backside of the target, spread the legs away from each other and then bend them towards the front of the target around the target legs as seen in the picture below. This keeps the legs from touching each other and helps hold the photoresistor snugly in the target.  Connect female ends of male to female wires to the legs of the photoresistor.

![Target Pic Front](/images/target_zoom.jpg)
![Target Pic Back](/images/target_back.jpg)
![Target Pic Front](/images/target_full.jpg)


Note: This is your first time playing with a laser in our lab, it hooks up just like an LED! The Red wire on the laser is positive and the blue wire is negative/ground.


Here is the wiring diagram:  

![Game Part 1 Diagram](/images/game_1_lab_bb.png)


Once you have the pico wired, take some time to attempt to code the points outlined in the overview using the old labs.

For coding the photoresistor, if you remove the **conversion_factor** we used in our lab, you will have a wide range of values. That is close to zero when there is no light, and close to 65535 under a super bright light.  This will give you a wide range to detect "normal" light conditions verses when the laser is shining directly on the photoresistor.
**WARNING** When working with the laser, DON'T SHOOT YOUR EYE OUT! Or anyone elses. :)

If you've given that a good effort and need a little guidance check out the code solution by clicking on the link below: 

<details><summary>Code!</summary> 

```Python

from machine import Pin,PWM,ADC
from math import modf
import utime

photoresistor_value = machine.ADC(28)

initial_photo_reading = photoresistor_value.read_u16()
print("Initial Laser Voltage Reading: ", initial_photo_reading)

laser = Pin(20, Pin.OUT)
laser.value(0)

button = Pin(17, Pin.IN, Pin.PULL_DOWN)

# debounce utime saying wait 5 seconds between button presses
DEBOUNCE_utime = 5000

# debounce counter is our counter from the last button press
# initialize to current utime
debounce_counter = utime.ticks_ms() - DEBOUNCE_utime
       
# Function to handle when the button is pressed
def button_press_detected():
    global debounce_counter
    current_utime = utime.ticks_ms()
    
    # Calculate utime passed since last button press
    utime_passed = utime.ticks_diff(current_utime,debounce_counter)

    # print("utime passed=" + str(utime_passed))
    if (utime_passed > DEBOUNCE_utime):
        print("Button Pressed!")
        # set debounce_counter to current utime
        debounce_counter = utime.ticks_ms()

        fire_the_laser()    
    #else:
        #print("Not enough utime")

def fire_the_laser():
    print("FIRE ZEE LASERS!")
    enable_laser()   
    check_target()     
    disable_laser()

def enable_laser():
    laser.value(1) 
    utime.sleep_ms(2000) 

def disable_laser():
    utime.sleep_ms(1000)   
    laser.value(0)

def check_target():
    global photo_reading
    photo_reading = photoresistor_value.read_u16()   
    print("Laser Voltage Reading: ",photo_reading)

# Below executes in the main(first) thread.
while True:

    if button.value()==True:
        button_press_detected()


```
</details>


If you got all of this to work, do your best Dr. Evil laugh at a volume that the instructors are sure to hear!
It's finally time for some sharks with some lasers on their heads.

