# First Input with Pico

## Overview

We will now use a GPIO (General Purpose Input/Output) pin on the Pico to detect when a button is pressed.  So, this will be our first time using a GPIO pin for input.  

We will create a circuit and the code to make the Blue LED light up only when you press the button.  However, unlike our first lab with the button, the LED and button will not be on the same circuit.  The button will simply be an input to the Pico and we will write code to control what happens when the button is pressed.

 ## What to do

Add your button back to the breadboard putting the far right pins of the button into column 40.  Remember to keep the slot under the button vertical (in line with the columns).  Connect the far right pin on column 40 to the positive power rail.  
Connect the left side of the button to the GP17 pin on the Pico which is in column 19 on the breadboard.

![Button Diagram](/images/8_button_pico_bb.png)



At this point the LED from the last lab should still be connected to GP16 and now the button is connected to GP17.  

Now to write the code to add the button management.  This just requires adding a line to initialize the button to be in a PULL_DOWN mode which means that GP17 pin acts as a ground.  So, when the button is pressed electricty can flow from the positive power rail through the button to the GP17 pin on the Pico which acts as a ground. Then in our code we can detect when this happens by checking the value of the button or GP17 pin.

Here's the code:

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
Enter the code above into the Thonny editor and then click the Play button.
If everything works, you should see the LED come on when you push and hold down the button.

If it works, slap yo self!

## Stretch Goal

Change the code above to make it so that when the button is pressed  the light flashes 3 times before turning off.

If you continue to hold the button down it should continue to flash.  

You may want to use a for loop. Here's Python for loop help: [Python For Loop with Range](https://www.w3schools.com/python/gloss_python_for_range.asp)

<details>
 <summary>To see working code for this click the arrow beside here to expand the code!</summary>
  

```Python
from machine import Pin
import utime

led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value()==True:
        print("Button Pressed!")
        for count in range(3):
            print("looping:" + str(count))
            led.value(1)
            utime.sleep_ms(400)
            led.value(0)
            utime.sleep_ms(400)
    else:
        led.value(0)
        
    
```

</details>

