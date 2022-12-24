# Three Lives and a Scoreboard

## Overview

In this grand finale for our game you will do the following:

- Add a seven segment display to keep score
- Add logic for a successful target hit:
  - Make your buzzer buzz a happy buzz
  - Add one point to the hit counter (make sure it updates on your seven segment display)
  - Increase the step of the pwm running in the thread to speed up your shark to make each level harder to beat
- Add logic for a missed laser fire:
  - Make your buzzer buzz a sad buzz
  - Darken one of the three LEDs (you start with 3 lives)
- Add logic for once you run out of lives to buzz a fun little buzz indicating the game has ended.


## What to do

TODO: Insert final diagram here with everything setup

![Game Finale Diagram](/images/needanimagehere.png)

![Game Stage Illustration](/images/needanimagehere.png)

Once you have the pico wired and the game stage set as seen above, take some time to attempt to code the points outlined in the overview using the old labs, building on your code from the Sharks With Laser Beams lab.

TODO: give helpful hint on setting a baseline photores value to determine if a hit happened or not from the laser

TODO: List some specific code snippets from previous labs to help guide them

TODO: Explain lining up the servo on the shark/ruler with a start/stop or a simple set degree command they can send in the console

**NOTE**<details><summary>If you've given that a good effort and need a little guidance check out the code solution by clicking here.</summary> 
```Python


from machine import Pin,PWM,ADC
import utime
import sg90
import _thread
import tm1637
from math import modf

photoresistor_value = machine.ADC(28)  # potential TODO - change PIN of photores
conversion_factor = 3.3/(65535)

# Initialize LEDs to on at beginning
# These LEDs indicate lives remaining
led1 = Pin(16, Pin.OUT)  # potential TODO - change PIN of LED
led1.value(1)
led1_on = True
led2 = Pin(18, Pin.OUT)  # potential TODO - change PIN of LED
led2.value(1)
led3_on = True
led3 = Pin(19, Pin.OUT)  # potential TODO - change PIN of LED
led3.value(1)
led3_on = True
lives_left = True

laser = Pin(20, Pin.OUT) # potential TODO - no idea if this is right.. also may need to change PIN
laser.value(0)

button = Pin(17, Pin.IN, Pin.PULL_DOWN) # potential TODO - change PIN of button

# Initialize Score and Display
display = tm1637.TM1637(clk=Pin(1), dio=Pin(0))  # potential TODO - change PIN of display
score = 0
display.number(score)

# Initialize Servo
sg90.servo_pin(15)
SMOOTH_TIME = 20
servo_speed = 1

# debounce utime saying wait 3 seconds between button presses
DEBOUNCE_utime = 3000

# debounce counter is our counter from the last button press
# initialize to current utime
debounce_counter = utime.ticks_ms()
       
def scan():
    stepping = servo_speed
    for i in range(90,180, stepping):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(180,89, -stepping):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)


    for i in range(90,-1,-stepping):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(0,91, stepping):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)
        
# define a function to execute in the second thread
def second_thread_func():
    while True:
        scan()
        print("servo_speed=", servo_speed)
        utime.sleep_ms(2000)
# Start the second thread
_thread.start_new_thread(second_thread_func,())

# Function to handle darkening one LED
def remove_led():
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
            # TODO - play game over jingle buzz
            
# Function to handle when the button is pressed
def button_press_detected():
    global debounce_counter
    current_utime = utime.ticks_ms()
    # Calculate utime passed since last button press
    utime_passed = utime.ticks_diff(current_utime,debounce_counter)
    print("utime passed=" + str(utime_passed))
    if (utime_passed > DEBOUNCE_utime):
        print("Button Pressed!")
        # set debounce_counter to current utime
        debounce_counter = utime.ticks_ms()

        initial_photo_reading = photoresistor_value.read_u16() * conversion_factor     
        print("Laser Voltage Reading: ",photo_reading)

        laser.value(1)  # TODO - no idea if this logic is right for firing the laser

        photo_reading = photoresistor_value.read_u16() * conversion_factor     
        print("Laser Voltage Reading: ",photo_reading)

        # TODO - might need a sleep here to allow time for reading??  utime.sleep_ms(400)
        laser.value(0)  # TODO - no idea if this logic is right for firing the laser

        variance = 1      # TODO - figure out proper variance for shot logic

        if (photo_reading > (initial_photo_reading + variance)):
          its_a_hit()
        else: 
          its_a_miss()
    
    else:
        print("Not enough utime")

def its_a_hit():
    # TODO - happy buzzer buzz
    servo_speed = servo_speed + 1
    score = score + 1
    display.number(score)

def its_a_miss():
    # TODO - sad buzzer buzz
    remove_led()

# Below executes in the main(first) thread.
while True:

    if (lives_left):
      if button.value()==True:
        button_press_detected()
    else:
      # TODO - game over logic... not sure if we need to explicitely do something here or not


```
</details>




If you got all of this to work, then go for a new high score!  and then another!  and then another!  and then another!


## References:

