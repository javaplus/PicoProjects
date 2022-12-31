# Blink External LED

## Overview

This will be a short one, we are simply going to blink an external LED.


 ## What to do

Grab your BLUE LED or any LED rated for 3volts.  Put the long pin into column 30 and then the short pin into column 31.  

Connect the short side to the ground/negative rail of the breadboard.
Connect the long side of the LED to column 20 which is GP16 pin of the Pico. "GP " stands for General Purpose Input Output.  You can refer to the Pico Pinout image to see the different GP pins of the Pico. Here's the reference image for the Pico Pinout: [Pico Pin Reference Page](/reference/pico_gpio.md)

![Blink Diagram](/images/7_blink_external_bb.png)


When the LED in place and connected to the Pico and to ground, then we just need to write the code.  However, this is the exact same code as last time, other than we need to change the Pin number from the onboard LED pin 25 to the GP16 pin.


``` Python
from machine import Pin
import utime

led = Pin(16, Pin.OUT)

while True:
    led.toggle()
    utime.sleep_ms(1000)
```
Enter the code above into the Thonny editor and then click the Play button.
If everything works, you should see the  LED flash about once a second.

If it works, blink twice!

## Other Pin functions.

Another way to turn the LED off and on is to use the [value() function](https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin.value).

Here is that code:

``` Python
from machine import Pin
import utime

led = Pin(16, Pin.OUT)

while True:
    led.value(1)
    utime.sleep_ms(1000)
    led.value(0)
    utime.sleep_ms(1000)
```

Try this out.  If you want it to blink faster change the time it sleeps.

