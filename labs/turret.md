# Turret!

Now that you know the basics of a joystick, we will make it control a turret made of servos!  

Before we start with the code, we have to wire our turret in. 

![turretDiagram](https://github.com/javaplus/PicoProjects/blob/main/images/turret6_bb.png?raw=true)



 We will then import a library for it to function. Let's will name it turret.py

 ```python
from machine import Pin, ADC
import machine
import utime
from sg90 import servo


class turret:

    
    def __init__(self, horizontal_servo_pin, vertical_servo_pin):
        self.servo_horiz = servo(horizontal_servo_pin)
        self.servo_vert = servo(vertical_servo_pin)
        
    def center(self):
        self.servo_horiz.move_to(90)
        self.servo_vert.move_to(90)
    
    # positive speed moves one direction and negative moves the other
    def move_left(self, speed):
        if (self.servo_horiz.position + speed) >= 0:
            self.servo_horiz.move_to(self.servo_horiz.position - speed)
            
    def move_right(self, speed):
        if (self.servo_horiz.position + speed) <= 180:
            self.servo_horiz.move_to(self.servo_horiz.position + speed)
            
    def move_up(self, speed):
        if (self.servo_vert.position + speed) <= 180:
            self.servo_vert.move_to(self.servo_vert.position + speed) 
        
    def move_down(self, speed):
        if (self.servo_vert.position + speed) >= 0:
            self.servo_vert.move_to(self.servo_vert.position - speed)
 ```

In this library we are making a class and functions for servo movement. This will help us easily move the servos without much knowledge about servos and joysticks. Defining the servos in our main code will give tell the library what servos to use. Now that we have our library, let's make the code. If you don't have the [SG90 Library](https://raw.githubusercontent.com/javaplus/PicoProjects/main/servos/sg90.py) already, go ahead and add it to a seperate file and name it sg90.
Now that you have the sg90 library, it will allow us to control the servo. Now we can start!

```python
from machine import Pin, ADC
import utime
from sg90 import servo
from turret import turret

SMOOTH_TIME = (20)

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(17,Pin.IN, Pin.PULL_UP)

#turret(servoXpin, servoYpin)
myturret = turret(15,14)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()

#recenters both servos
    if buttonValue == 0:
        myturret.center()

#myturret.move_(direction)(movement_speed)
    if xValue <= 600:
        myturret.move_right(5)
   
    if xValue >= 65000:
        myturret.move_left(5)
         
    if yValue <=600:
        myturret.move_up(5)
        
    if yValue >= 65000:
        myturret.move_down(5)
        
    utime.sleep_ms(SMOOTH_TIME)           
```

  What we're doing here is calling functions in the turret library to make the turrets move.
