# Blink the Onboard LED

## Overview

We've finally made it to our first lab with actually using the Pico as a microcontroller and not as just a power source.  We will write our first bit of code in Python to have the Pico flash it's onboard LED!  This is the obligatory blink demo for nearly all microcontroller projects... this is the equivalent of the "hello world" program.

## Raspberry Pi Pico H

We are using the Raspberry Pi Pico H which is part of the Pi Foundations new Microcontroller family of boards... You can read more about them here.

[Official Pico Page](https://www.raspberrypi.com/products/raspberry-pi-pico/)

 ## What to do

To start you don't need anything but the pico for this lab.  So, feel free to strip everything else off except the Pico. I would leave the wires connecting the Pico to the power rails although technically they are not needed for this lab.

![Blink Diagram](/images/6_blink_bb.png)

With the breadboard cleared, and the Pico still connected to your USB port, open Thonny and in the bottom right hand corner choose the interpreter for Thonny to use.  If your computer recognized the Pico, you can choose the item that says "**MicroPython(Raspberry Pi Pico)** in the list. (see image below)

![Thonny Select Pico](/images/thonny_pico.PNG)

If having issues connecting see if this detailed guide helps: 
[Detailed guide for connecting Pico to Thonny](https://microcontrollerslab.com/getting-started-raspberry-pi-pico-thonny-ide/)


It it's able to connect, you should see the print out in the shell like in the picture above that tells you the version of MicroPython running on the Pico.
The shell below is a [REPL](https://pythonprogramminglanguage.com/repl/) where you could type Python statements have them executed immeditately.  We are not going to use the shell.  Instead, we will type our code into the text editor area above the shell.

Here is the obligatory blink demo for the Pico:

``` Python
from machine import Pin
import utime

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    utime.sleep_ms(1000)
```
Enter the code above into the Thonny editor and then click the Play button.
If everything works, you should see the onboard LED flash green about once a second.

If it works, eat a snack or better yet, give your instructor one!

If the instructor didn't explain each line of the code or it doesn't make sense, throw something at him/her and make them explain it!

