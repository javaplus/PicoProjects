# Button Interrupt vs Polling

## Overview

Like the last lab, we are going to work on another programming technique when dealing with input from buttons.  Last time we dealt with debouncing our button input, this time we are going to look at the **polling** vs **interrupt** method for reading input.  

Our current while loop (see below) is constantly checking the **button.value()** to see if the button is pressed.
``` Python
...
...
while True:
    if button.value()==True:
        button_press_detected()
```
This constant checking of the button value is called **polling**.  It uses CPU cycles to constantly check the button state.  A better way of doing this is using **interrupts**.  Using the interrupt approach we can actully have the hardware (the GPIO pin) notify us of when something happened.  It's kind of like event driven programming. The microcontroller will interrupt the main thread of the program to say something happened.


 ## What to do

In case you messed up or re-arranged your breadboard since the last lab, here is what your breadboard should look like:
![Button Diagram](/images/8_button_pico_bb.png)


So, using an interrupt on the Pico with MicroPython is easy.  We will simply create a function to be called when the button is pressed.  This will be like a callback function that gets invoked when the Pico detects a change on the GPIO pin connected to the button.

Here I'll show some of new parts of the code we will be adding and then I'll show the full code below.
We are going to start by adding a global flag that tells when the button was pressed and then a function to set the flag when the interrupt detects a button press.
```Python

# define flag to say when button is pressed:
button_pressed = False

# define function to be called when button is pressed
def button_interrupt_handler(pin):
    # since this is called by an interrupt do very little
    # need to give control back to CPU quickly.
    # Could possibly do debounce work here???
    global button_pressed
    button_pressed = True

## define interrupt to call our function when button is pressed:
button.irq(trigger=Pin.IRQ_RISING, handler=button_interrupt_handler)

```
In the snippet of code above, you can see our boolean flag to define when the button is pressed.  
Then the function **button_interrupt_handler()** that is simply setting that flag to true.
Our **button_interrupt_handler()** is passed as the handler to our **irq** function call to set up the interrupt monitor.

After this we just need to update our while loop to use this new flag instead of polling the button value each time and then we refactor our existing **button_press_detected()** function to set this button_pressed flag to False at appropriate times.

Here's the full code:

``` Python
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

# define flag to say when button is pressed:
button_pressed = False

# define function to be called when button is pressed
def button_interrupt_handler(pin):
    # since this is called by an interrupt do very little
    # need to give control back to CPU quickly.
    # Could possibly do debounce work here???
    global button_pressed
    button_pressed = True

## define interrupt to call our function when button is pressed:
button.irq(trigger=Pin.IRQ_RISING, handler=button_interrupt_handler)    

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
    global debounce_counter, button_pressed
    current_utime = utime.ticks_ms()
    # Calculate utime passed since last button press
    utime_passed = utime.ticks_diff(current_utime,debounce_counter)
    print("utime passed=" + str(utime_passed))
    if (utime_passed > DEBOUNCE_utime):
        print("Button Pressed!")
        # set debounce_counter to current utime
        debounce_counter = utime.ticks_ms()
        toggle_led()
        button_pressed=False
    
    else:
        button_pressed = False
        print("Not enough utime")

while True:
    if button_pressed==True:
        button_press_detected()
  
```
Enter the code above into the Thonny editor and then click the STOP button to reset and then click the Play button to run the new code.

Try pressing the button to toggle the LED on and off.
If everything is working, then you should see the button toggle off and on as you press and release the button.

If it works, interrupt someone else by shouting "It's working!  It's working!"


## References

If you'd like to read more about the **irq()** function or other **Pin** functions here's the link to the official docs:  
[Pin Documentation](https://docs.micropython.org/en/latest/library/machine.Pin.html)

