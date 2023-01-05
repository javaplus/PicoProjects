# FIRE ZEE LASERS!!!!1!!

## Overview

You are now well prepared for our final objective.  What's a mad scientist pre-compiler without a little fun with lasers and target practice??

In this part 1 of 3 for our final game you will do the following:

- Wire the photo resistor through the two little holes in the middle of your target and place the target end cap on one end of the ruler with the photo resistor side facing towards the rest of the ruler
- Detect a button press (use various button labs as a reference)... if this happens the pico should FIRE ZEE LASER and the photores (our target) needs to read the current value (use various button labs as a reference).
- Once the button has been pressed we need to lock out the player from another attempt for 5 seconds (use debounce lab as a reference)

  
 ## What to do

TODO: Insert diagram here of breadboard with button, laser, andd photores connected

![Game Part 1 Diagram](/images/needanimagehere.png)


Note: This is your first time playing with a laser in our lab, it hooks up just like an LED!

Once you have the pico wired, take some time to attempt to code the points outlined in the overview using the old labs.

Code<details><summary>If you've given that a good effort and need a little guidance check out the code solution by clicking here.</summary> 
If using the Pico W the internal pin for the LED is NOT 25.  It's the string "LED". So, assuming you flashed your Pico W with the right MicroPython library(the one for the Pico W), then the led line above would look like this for the Pico W:
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
debounce_counter = utime.ticks_ms()
       
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


If you got all of this to work, do your best Dr. Evil laugh at a volume that the instructors are sure to hear!  It's finally time for some sharks with some lasers on their heads.

