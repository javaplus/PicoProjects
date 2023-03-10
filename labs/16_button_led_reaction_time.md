# Using a button and LED to create a reaction time game

## Overview

Lets use what we learned in lab 8 to create a simple game with only a button and an LED. Our goal is to light up the LED after a random amount of time and then capture how long it takes the player to press the button. Once we've captured the time, in milliseconds, print it to the screen. 



 ## What to do

Lets wire this exactly how Lab 8 is wired!

Grab your BLUE LED or any LED rated for 3volts.  Put the long pin into column 30 and then the short pin into column 31.

Add your button back to the breadboard putting the far right pins of the button into column 40.  Remember to keep the slot under the button vertical (in line with the columns).  Connect the far right pin on column 40 to the positive power rail.  
Connect the left side of the button to the GP17 pin on the Pico which is in column 19 on the breadboard.

![Button Diagram](/images/8_button_pico_bb.png)


Lets start with the code from lab 8 which will turn the LED on when the button is pressed. Obviously this won't work for this lab, but it's a great starting point.

Here's the starting code:

``` Python
from machine import Pin

led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value()==True:
        print("Button Pressed!")
        led.value(1)
    else:
        led.value(0)
        
    
```

We will need to use the `random` library to generate a random time to wait before turning on the LED, here's how you do that

``` Python
import random
# Generate a random delay between 1 and 5 seconds
delay = random.randint(1, 5)
```

We will need to wait that random amount of time and also calculate how long it took for the player to press the button with the `utime` library, here's how

``` Python
import utime

# Wait for the random delay
utime.sleep(delay)

# Capture the current time
start_time = utime.ticks_ms()
```

Take these few hints and see if you can implement the rest of the game.

<details>
 <summary>Don't worry if you can't. Click here to see working code!</summary>

``` Python
import utime
import random
from machine import Pin

# Set up the LED pin
led = Pin(16, Pin.OUT)

# Set up the button pin
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

# Turn off the LED incase it's already on
led.off()

# Generate a random delay between 1 and 5 seconds
delay = random.randint(1, 5)

# Wait for the random delay
utime.sleep(delay)

led.on()

start_time = utime.ticks_ms()
# Wait for the user to press the button
while not button.value():
    pass
end_time = utime.ticks_ms()

# Calculate and display the time taken to press the button
duration = end_time - start_time
print("Button pressed after", duration, "milliseconds!")

led.off()
```
</details>

Play the game a few times and then yell out your fastest reaction time!

## Stretch Goal

Change the code above so the game automatically restarts so you don't have to press Run in Thonny everytime

<details>
 <summary>To see working code for this click the arrow beside here to expand the code!</summary>
  

```Python
import utime
import random
from machine import Pin

# Set up the LED pin
led = Pin(16, Pin.OUT)

# Set up the button pin
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

while True:
    # Turn off the LED incase it's already on
    led.off()
    
    # Generate a random delay between 1 and 5 seconds
    delay = random.randint(1, 5)

    # Wait for the random delay
    utime.sleep(delay)

    led.on()

    start_time = utime.ticks_ms()
    # Wait for the user to press the button
    while not button.value():
        pass
    end_time = utime.ticks_ms()

    # Calculate and display the time taken to press the button
    duration = end_time - start_time
    print("Button pressed after", duration, "milliseconds. The game will automatically restart")
    
    led.off()
    utime.sleep(2)
```
</details>
