import machine
import utime
import sg90

servo = machine.PWM(machine.Pin(1))
servo.freq(50)



def move_servo_to_angle(pin,angle):

    duty = sg90.duty_cycle_for_angle(angle)
    pin.duty_u16(duty)


move_servo_to_angle(servo, 90)
utime.sleep_ms(1000)

move_servo_to_angle(servo, 45)
utime.sleep_ms(1000)

move_servo_to_angle(servo, 0)
utime.sleep_ms(1000)

move_servo_to_angle(servo, 45)
utime.sleep_ms(1000)

move_servo_to_angle(servo, 90)
utime.sleep_ms(1000)

move_servo_to_angle(servo, 130)
utime.sleep_ms(1000)

move_servo_to_angle(servo, 180)
utime.sleep_ms(1000)

move_servo_to_angle(servo, 130)
utime.sleep_ms(1000)

move_servo_to_angle(servo, 90)
utime.sleep_ms(1000)



