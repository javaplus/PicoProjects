import utime
import sg90

sg90.servo_pin(15)


SMOOTH_TIME = 20



def scan():
    for i in range(90,180):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(180,89, -1):
        print(i)
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)


    for i in range(90,-1,-1):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(0,91):
        print(i)
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

sg90.move_to(90)

while True:
    scan()




