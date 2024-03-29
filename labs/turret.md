# Turret!

Now that you know the basics of a joystick we will make it control a servo!  

Before we start with the code we have to wire our turret in.


 first we will import a library for it to function we will name it turret.py

 ```python
from machine import Pin, ADC
import machine
import utime
from sg90 import servo


class turret:

    
    def __init__(self, horizontal_servo_pin, vertical_servo_pin):
        self.servo_horiz = servo(horizontal_servo_pin)
        self.servo_vert = servo(vertical_servo_pin)
    
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

this library will allow the servo to easily move! Now we got our library lets make the code. If you don't have the [SG90 Library](https://raw.githubusercontent.com/javaplus/PicoProjects/main/servos/sg90.py) already go ahead and add it to a seperate file and name it sg90.
Now that you have the sg90 library it will allow us to control the servo, now we can start!

```python
from machine import Pin, ADC
import utime
from sg90 import servo
from turret import turret

SMOOTH_TIME = (20)

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(17,Pin.IN, Pin.PULL_UP)

myturret = turret(15,14)
myturret.servo_horiz.move_to(90)
myturret.servo_vert.move_to(90)
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    
    if buttonValue == 0:
        myturret.servo_horiz.move_to(90)
        myturret.servo_vert.move_to(90)
        
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

