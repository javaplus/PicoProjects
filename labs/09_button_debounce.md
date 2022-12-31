# Button Debounce

## Overview

We are going to work on some programming techniques now when dealing with reading input especially from a button.  So, we won't be changing our wiring for this lab we will just be working on code.

Our goal for this lab is to use our button to toggle the LED from off to on and vice versa.  That is if the LED is off, pressing and releasing the button should turn it on and leave it on.  Then to turn the LED off again, we would press and release the button again to turn it off.

 ## What to do

In case you messed up or re-arranged your breadboard since the last lab, here is what your breadboard should look like:
![Button Diagram](/images/8_button_pico_bb.png)

To allow our button to be a toggle to turn our LED off or on update your code to match this:

Here's the code:

``` Python
from machine import Pin


led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

led.value(0) # init led to off
# Flag for if LED is on or off
led_on = False

while True:
    if button.value()==True:
        print("Button Pressed!")
        if(led_on):
            led.value(0)
            led_on = False
        else:
            led.value(1)
            led_on = True
        
    
```
Enter the code above into the Thonny editor and then click the STOP button to reset and then click the Play button to run the new code.

Try pressing the button to toggle the LED on and off.  The idea is that if you tap the button when the LED is off, it should then come on.  Then if the LED is on, pressing and releasing the button should turn it off.  However, if you try it out, you should notice some inconsistency.  That is it probably won't work consistently.  Try pressing and releasing the button several times and see what happens.  Can you identify the cause of the inconsistency?

<details>
 <summary>Click here when you are ready to read about the issue.</summary>

 The issue is what we call button bouncing.  The while loop is running at such a fast pace that when you press the button it triggers multiple button presses.  There is no pause in our code from the time it detects one button press til the time it tries to check again.  So, if the button is held down for just a few milliseconds, it could trigger multiple button presses.
</details>

### Button Bounce Fix

Fixing this issue is called "debouncing".  One of the easiest ways to do this is by keeping track of the time from when the button was pressed before you register another button press.  That is we can keep a timer that starts when we detect a button press and then not take any action unless a certain time passes before the next button press.

In our code, we will now create a debounce_timer flag to keep track of the time when the button is pressed and only allow another button press after 500 milliseconds.

If you'd like to try it yourself without copying our code, you may find the documentation for the [time library](https://docs.micropython.org/en/latest/library/time.html#module-time) helpful.  NOTE: time and utime are the same.  Importing time is the same as importing utime.  
The **ticks_ms()** and the **ticks_diff()** function are useful.

<details>
 <summary>To see working code for this click the arrow beside here to expand the code!</summary>
  

```Python
from machine import Pin
import time

led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

led.value(0) # init led to off
# Flag for if LED is on or off
led_on = False


# debounce TIME saying 500ms between button presses
DEBOUNCE_TIME = 500
# debounce counter is our counter from the last button press
# initialize to current time
debounce_counter = time.ticks_ms()

while True:
    if button.value()==True:
        current_time = time.ticks_ms()
        # Calculate time passed since last button press
        time_passed = time.ticks_diff(current_time,debounce_counter)
        print("time passed=" + str(time_passed))
        if (time_passed > DEBOUNCE_TIME):
            print("Button Pressed!")
            # set debounce_counter to current time
            debounce_counter = time.ticks_ms()
            if(led_on):
                led.value(0)
                led_on = False
            else:
                led.value(1)
                led_on = True
        else:
            print("Not enough time")
    
```

</details>


### Run it!

After adding your debounce logic, you should be able to run it and see that pressing and releasing the button now consistently toggles the LED off and on.

If this works, give someone nearby a high five!

### Clean Code

**NOTE** Our code is getting a little messy so it would be nice to move some logic into functions.  Feel free to refactor and clean it up yourself or copy our example.

```Python
from machine import Pin
import utime

led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

led.value(0) # init led to off
# Flag for if LED is on or off
led_on = False


# debounce utime saying 500ms between button presses
DEBOUNCE_utime = 500
# debounce counter is our counter from the last button press
# initialize to current utime
debounce_counter = utime.ticks_ms()

# Function to handle turning LED off and on and setting flag
def toggle_led():
    global led_on
    if(led_on):
        led.value(0)
        led_on = False
    else:
        led.value(1)
        led_on = True

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
        toggle_led()
    
    else:
        print("Not enough utime")


while True:
    if button.value()==True:
        button_press_detected()

```

After making the above changes, test you code again to make sure it still works.  Having easy to understand code as well as single purpose functions is key to being able to continue to add features quickly and maintian and debug your code.
