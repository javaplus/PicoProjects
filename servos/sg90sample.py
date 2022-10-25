import sg90
import utime

sg90.servo_pin(15)

#Center
sg90.move_to(90)
utime.sleep_ms(1000)

#move_to to one extreme
sg90.move_to(0)
utime.sleep_ms(1000)

#move_to to other extreme
sg90.move_to(180)
utime.sleep_ms(1000)

#Center
sg90.move_to(90)
