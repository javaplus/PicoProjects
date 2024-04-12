# Joysticks

## How do Joysticks work?

![Joystick](https://m.media-amazon.com/images/I/71KNhxKbNBL._AC_SX425_.jpg)
  
  Joysticks are input devices that move on a base which communicates the angle to the device its controlling.
  Joysticks are commonly used in controllers and aviation cockpits. Joysticks detect input direction
  with eletronic switches, Hall effect, strain guage or potentiometers but most controllers today seem to use
  potentiometers.

## Getting started!

The joystick for this lab uses potentiometers internally and can detect movement in the x axis, the why axis, and can detect when the joystick is pushed in like a button. 
 The joystick will have 5 pins: 5v, ground, vrx(voltage proportional to X axis), vry(voltage proportional to y axis) and sw(switch). We will need to use the 5v on the pico to power a rail, then after that connect 
the ground pin. Now let's connect the vrx, switch, and vry. Vrx will go in GPIO pin 27, Switch in GPIO pin 17 and vry in GPIO pin 26 like shown in the picture.  
![JoystickDiagram](https://github.com/javaplus/PicoProjects/blob/main/images/joystick%202_bb.png?raw=true)  

Now that we have it wired in, we can now write the code that will read the joysticks input and print out the values based on it's motion. Now let's code this puppy up!

```python
#code from https://www.youtube.com/watch?v=SJr-HoCwlWg
from machine import Pin, ADC
import utime

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(17,Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    buttonStatus = "not pressed"


    if buttonValue == 0:
        buttonStatus = "pressed"
        
        
    print("X: " + str(xValue) + ", Y: " + str(yValue) + " -- button value: " + str(buttonValue) + " button status: " + buttonStatus)
    utime.sleep(0.2)

```
Now try running the code above. You should see a steady stream of statements in the console telling you the x and y values as well as if the joystick is pressed.
Increase the value passed to `utime.sleep()` if you want the print statements less frequent, but understand this will mean that the position of your joystick will be read less often.

Notice the x and y values as the code runs and you move the joystick around.  
**NOTE** Most cheap joysticks like the one you probably have may have a dead zone around the center or even worse "freak out" when the joystick is pushed to its max range in some directions.  We've noticed that most of the cheaper joysticks when pushed to the extent of their movement in one direction will often falsely show an extreme movement on the other axis as well.  That is if you push the joystick full left, it will also show the the joystick is pulled down even if their is now downward movement on the joystick.  So, the key understanding here is that electronics can have flaws in them and a lot of cheap electronics don't always work as advertised.  So, when running the simple code above watch the values closely and understand the max ranges and sensitivity of your particular joystick.  This will help you better write code to handle any peculiarities it may have.

## Detecting Direction

Now let's modify the code slightly by checking the x and y values to try to determine the direction of the joystick.  That is we will use the values we read to determine if the joystick is being pushed side to side or up and down. 

Feel free to try to write the code on your own to detect when the joystick is moved left, right, up, or down.  An easy way is to just use if statement comparing the values of the x and y values read from the joystick.  

If you'd like to see how to code it we have some code below.
Now let's make more code to further your understanding!

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
 
the code checks the axis values to see if the joystick have passed those positions and if so will print the direction of the joystick.
    
 [you can learn more about joystick here](https://lastminuteengineers.com/joystick-interfacing-arduino-processing/)

