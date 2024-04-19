# One Simple Request: Sharks with Frickin Laser Beams

## Overview

In this part 2 of 3 for our final game you will do the following:

- Setup the game stage on our trusty rulers (image below)
- Mount the laser to your sharkhead
- Mount the servo on the ruler end cap
- Mount the shark on the servo (see below for setting "home" on your servo)
- Add code that will pan our servo back and forth (in its own thread)
- Add code to manage the lighting of 3 LEDs.  Each LED will represent a "life" during our game.  They should all be turned on by default.
- Create a function that will turn off one of the remaining lit LEDs.  We will use this later on in lab F03 when we determine that we missed one of our laser shots.
- Within your scan method you should have a way to detect if the laser has been fired (button was pressed). The servo should stop moving when this happens.  (Hint: implement a global kill_flag)

## What to do

### Set up the Shark:

Install the laser into the shark head.  You will have to disconnect your laser (the short wires) from the male-to-female wires to feed the laser wires down through the hole in the top of the shark head.  Once the laser wires come out the bottom of the shark, reconnect them to the female ends of the male-to-female wires that go to the breadboard.

Now install the servo **upside down** into the shark (image below).  The wires for the laser and the wires for the servo, should go towards the front of the shark.  There is a notch in the bottom of the shark model under the hole for the laser wires that should allow the laser wires and the servo wires to not get in the way of pushing the servo up into the shark.
#### Bottom side of Shark:
![Shark Bottom](/images/shark_bottom.jpg)  

**NOTE** If the servo isn't snug in the bottom of the shark you can add some tape around the base of the servo which goes up into the shark to make it fit nice and tight.


### Setting a home direction for the laser

Now connect the servo's power wire(red middle) to the 5volt rail. Connect the servo's ground wire (dark brown) to any ground(-) rail.  Connect the orange/yellowish signal wire of the servo to GP15 which is Column 20 on the bottom side of the Pico. If need be, reference the [wiring diagram](#wiring-to-the-pico) further down the page.  
**BEFORE** snapping the servo onto the base, run the following code in the shell of Thonny to allow us to set a "home" for the shark and align the laser.

```Python
from sg90 import servo

servo1 = servo(15)
servo.move_to(90)

```

After this code is run and your servo adjusts to 90, place the servo into the end cap on the ruler. Pointing straight towards your target at the other end.  

![Shark Side](/images/shark_side.jpg)

After snapping the shark servo onto the base and sliding it on the ruler, we can aim the laser.  So, connect the laser back up with the red wire going to GP20 and the blue wire to ground.  Once connected run this code in the terminal to turn on the  laser.

```Python
from machine import Pin

laser = Pin(20, Pin.OUT)
laser.value(1)

```

Your setup should look like this now with the laser on and hitting the target:  

![Game Stage Illustration](/images/gamestage.png)

With the laser on, adjust it up and down to hit the center line of the target.  The laser doesn't need to hit the bullseye(photoresistor) directly at this time.  The laser just needs to hit at the same height as the bullseye.  For our game, the shark will rotate back and forth and you will have to stop the shark and "fire" the laser at the right time to hit the bullseye. So, at this time just make sure the laser is not hitting high or low... left and right of the bullseye is ok if it's at the same height as the bullseye.


## Wiring to the Pico

 Here is the wiring diagram with the additions for this lab. **NOTE** The top half of the diagram remains the same from the last lab.  The additions are all on the bottom half of the breadboard with the exception of the wires connecting the 3 LEDS to the Pico cross over the top half of the breadboard to the Pico's GP pins (GP19,GP18, and GP17).  

![Game Part 2 Diagram](/images/game_2_lab_bb.png)


##  Get your hands dirty

Once you have the pico wired and the game stage set as seen above, take some time to attempt to code the points outlined in the overview using the old labs, building on our code from the Fire Zee Lasers Lab.

**Code!**<details><summary>If you've given that a good effort and need a little guidance check out the code solution by clicking here.</summary> 
```Python


from machine import Pin,PWM,ADC
from math import modf
import utime, _thread, tm1637, sys
from sg90 import servo

photoresistor_value = machine.ADC(28)

# Initialize LEDs to on at beginning
# These LEDs indicate lives remaining
led1 = Pin(16, Pin.OUT)
led1.value(1)
led1_on = True
led2 = Pin(18, Pin.OUT)
led2.value(1)
led2_on = True
led3 = Pin(19, Pin.OUT)
led3.value(1)
led3_on = True
lives_left = True

laser = Pin(20, Pin.OUT)
laser.value(0)

button = Pin(17, Pin.IN, Pin.PULL_DOWN)

# Initialize Servo
servo1 = servo(15)
SMOOTH_TIME = 80
servo_speed = 1

# flag so the laser can interrupt the scan cycle
kill_flag = False

# debounce utime saying wait 5 seconds between button presses
DEBOUNCE_utime = 5000

# debounce counter is our counter from the last button press
# initialize to current utime
debounce_counter = utime.ticks_ms() - DEBOUNCE_utime
       
def scan(current_servo):
    stepping = servo_speed
    for i in range(45,130, stepping):
        if (kill_flag):
            break
        current_servo.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(130,45, -stepping):
        if (kill_flag):
            break
        current_servo.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)
        
# define a function to execute in the second thread
def second_thread_func():
    while True:
        # fix for import failing in second thread when it's inside a function
        servo2 = servo1
        stepping = servo_speed
        scan(servo2)
        #print("servo_speed=", servo_speed)
        utime.sleep_ms(100)

# Start the second thread
_thread.start_new_thread(second_thread_func,())

# Function to handle darkening one LED
def remove_led():
    global led3_on, led3, led2_on, led2, led1_on, led1, lives_left
    if(led3_on):
      led3.value(0)
      led3_on = False
    else:
        if(led2_on):
          led2.value(0)
          led2_on = False
        else:
            led1.value(0)
            led1_on = False
            lives_left = False
            end_of_game_buzz()
            
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
    global servo_speed

    enable_laser()   
    check_target()     
    disable_laser()

def enable_laser():
    global kill_flag
    kill_flag = True
    laser.value(1) 
    utime.sleep_ms(2000) 

def disable_laser():
    global kill_flag
    utime.sleep_ms(1000)   
    kill_flag = False
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



If you made it this far, stand up, stretch, and give someone a fist bump!
