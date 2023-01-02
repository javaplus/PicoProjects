from sg90_class import SG90
import time

servo = SG90(15)


servo.move_to(90)
time.sleep(1)



servo.move_to(40)
time.sleep(1)


servo.move_to(130)
time.sleep(1)


servo.move_to(90)
time.sleep(1)


servo.move_to(40)
time.sleep(1)

servo.move_to(130)
time.sleep(1)


servo.move_to(90)






