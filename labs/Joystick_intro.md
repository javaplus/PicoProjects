# Joysticks

## How do Joysticks work?

![Joystick](https://m.media-amazon.com/images/I/71KNhxKbNBL._AC_SX425_.jpg)
  
  Joysticks are Input devices that moves on a base and tells its angle to the device its controlling.
  Joysticks are commonly used in controllers and aviation cockpits. Joysticks detect input direction
  with eletronic switchs, Hall effect, strain guage or potentiometers but most controllers today seem to use
  potentiometers.

## Getting started!

The controller will have 5 pins: 5v, ground, vrx(voltage proportional to X axis), vry(voltage proportional to y axis) and sw(switch). We will need to use the 5v on the pico to power a rail, then after that connect 
the ground pin. Now lets connect the vrx, switch, and vry. vrx will go in GPIO 27, Switch in GPIO 17 and vry in GPIO 26  

```python
#modified code from https://www.youtube.com/watch?v=SJr-HoCwlWg
from machine import Pin, ADC
import utime

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(17,Pin.IN, Pin.PULL_UP)
# while loop to keep checking conditioning
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    
# Check the x and y Value to determine the status of the joystick
    if buttonValue == 0:
        buttonStatus = "pressed"
        
    if xValue <= 600:
        xStatus = "left"
        
    if xValue >= 60000:
        xStatus = "right"
        
    if yValue <= 600:
        yStatus = "up"
        
    if yValue >= 60000:
        yStatus = "down"
        
   
    #printing directions of the joystick
    print("X: " + xStatus + ", Y: " + yStatus + "  button status: " + buttonStatus)
    utime.sleep(0.2)
```
 
  
    
 [learn the ins and outs of joysticks!](https://components101.com/modules/joystick-module)  

 the values with axis see if the joystick have passed those positions and if so will give the direction of the joystick. right = x60000 position, left x600, up y600 and down y60000.
