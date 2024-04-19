from machine import Pin, ADC
import utime
from turret import turret

laser = Pin(16, Pin.OUT)

laser.value(1)

led = Pin(13, Pin.OUT)

photoresistor_value = machine.ADC(28)

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
    photo_reading = photoresistor_value.read_u16()

#recenters both servos
    if buttonValue == 0:
        myturret.center()

#Adjust x and y values based on sensitivity of your joystick
#myturret.move_(direction)(movement_speed)
    if xValue <= 48000:
        myturret.move_right(1)
        
    if photo_reading <= 15000:
        led.value(1)
        
    if not photo_reading <= 15000:
        led.value(0)
   
    if xValue >= 54000:
        myturret.move_left(1)
         
    if yValue <=46500:
        myturret.move_up(1)
        
    if yValue >= 54000:
        myturret.move_down(1)
        
    utime.sleep_ms(SMOOTH_TIME)           
