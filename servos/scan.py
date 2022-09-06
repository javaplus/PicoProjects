import machine
import utime
import sg90

servo = machine.PWM(machine.Pin(1))
servo.freq(50)



SMOOTH_TIME = 20


def move_servo_to_angle(pin,angle):

    duty = sg90.duty_cycle_for_angle(angle)
    pin.duty_u16(duty)

def scan():
    for i in range(90,180):
        move_servo_to_angle(servo, i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(180,89, -1):
        print(i)
        move_servo_to_angle(servo, i)
        utime.sleep_ms(SMOOTH_TIME)


    for i in range(90,-1,-1):
        move_servo_to_angle(servo, i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(0,91):
        print(i)
        move_servo_to_angle(servo, i)
        utime.sleep_ms(SMOOTH_TIME)

move_servo_to_angle(servo, 90)

while True:
    scan()



