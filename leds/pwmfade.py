import machine
import utime

led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
    
    # Fade up in brightness
    for i in range(0,65535):
        #print(i)
        led.duty_u16(i)
        utime.sleep(.0001)

    # Fade down in brightness
    for x in range(65535,0,-1):
        #print(x)
        led.duty_u16(x)
        utime.sleep(.0001)

