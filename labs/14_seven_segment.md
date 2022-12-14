# 7 Segment Display

## Overview

Output voltage to 7 segment.


## Working with Analog inputs 

Save on Pico as **tm1637.py**.
[TM1637 library](https://github.com/mcauser/micropython-tm1637/blob/master/tm1637.py)

![ADC GPIO Pins](/images/adcpins.PNG)


 ## What to do

  
  


###### Wiring Diagram
![Servo Diagram](/images/14_seven_segment_bb.png)


Once everything is wired, we will write the code to work with GPIO pin #28 and configure it as an ADC input.  We will read the values from it and use a simple formula to convert that to a volage reading.  

You can copy the simple code below to display the values read from the photoresistor.

Here's the code:

``` Python
from machine import Pin, ADC
import tm1637
import utime
from math import modf

display = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
 
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


## Optional Stretch goal


## References:
