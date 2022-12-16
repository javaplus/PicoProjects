# 7 Segment Display

## Overview

We are going to get into the exciting world of 7 segment displays.
##### TM1637 7 Segment Display
![TM1637 7 Segment Display](/images/tm1637.jpeg)

7 Segment displays are called such because each number is made up of 7 little bars or segments.  These are perfect for outputting any number and even some words/letters.

We are going to learn to use our 7 segment display to output the voltage level read from our photoresistor.


## TM1637 7 Segment Display

The 7 segment display we are working with is the [TM1637](https://www.amazon.com/HiLetgo-Digital-Segment-Display-Arduino/dp/B01DKISMXK/ref=sr_1_1_sspa?keywords=tm1637&qid=1671206265&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRVUwNTVUTTQyVUEmZW5jcnlwdGVkSWQ9QTA5OTU4NDVITEZHSkYzRzBNRUQmZW5jcnlwdGVkQWRJZD1BMDU1NjUxNzI2SVNONk5XSjkzNkQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl). The TM1637 display is actually named after the [drive control integrated circuit](https://www.makerguides.com/wp-content/uploads/2019/08/TM1637-Datasheet.pdf) that drives the LEDs.  It's this circuit that makes it possible to only use 2 signal pins to control all the segments. (The other two pins are for power).

## What to do

To use the TM1637 7 segment display, we are going to do what any good developer does and steal...uhmm... borrow someone else's library that makes it super simple to work with the display.

We aren't stealing, **MCAUSER** on github was kind enough to make a MicroPython compatible library available for anyone to use.  Go to the tm1637 library here: [TM1637 library](https://github.com/mcauser/micropython-tm1637/blob/master/tm1637.py) and copy it's contents into a new file in Thonny and save on Pico as **tm1637.py**.

Now follow the diagram below to wire the 7 segment display up to the Pico.

###### Wiring Diagram
![Servo Diagram](/images/14_seven_segment_bb.png)


Once everything is wired, we will write the code to work with GPIO pin #0 and #1.  We are still using the same code to read the voltage from the Photoresistor, but we will add the code to use our tm1637 library to write those values out to the display.

You can copy the simple code below to display the values read from the photoresistor.

Here's the code:

``` Python
from machine import Pin, ADC
import tm1637
import utime
from math import modf

display = tm1637.TM1637(clk=Pin(1), dio=Pin(0))
 
photoresistor_value = machine.ADC(28)
conversion_factor = 3.3/(65535)

def split_voltage(volts):
    voltage_rounded = round(volts, 2)
    print("Rounded:", voltage_rounded)
    dec,whole = modf(voltage_rounded)
    whole = int(whole)
    dec = int(dec * 100)
    return dec, whole

def write_voltage_to_dispay(volts):
    # round voltage to 2 digits after decimal
    dec_num,whole_num=split_voltage(volts)
    print("whole", whole_num)
    print("dec", dec_num)
    display.numbers(whole_num, dec_num, True)
    

while True:
    photo_reading = photoresistor_value.read_u16() * conversion_factor     
    print("Voltage Reading: ",photo_reading)
    display.numbers(12,34, True)
    write_voltage_to_dispay(photo_reading)
    utime.sleep(0.2)  


```

Run the code and test it!

If it works, display your biggest grin on your face!

## References:

[Test Library for TM1637 from MCAUSER](https://raw.githubusercontent.com/mcauser/micropython-tm1637/master/tm1637_test.py)