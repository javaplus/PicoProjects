from machine import Pin,PWM,ADC
from math import modf
import utime, sg90, _thread, tm1637, sys

photoresistor_value = machine.ADC(28)

initial_photo_reading = photoresistor_value.read_u16()
print("Initial Laser Voltage Reading: ", initial_photo_reading)

# target will recognize a hit when there is a 20% increase in light
target_reading = initial_photo_reading * 1.2   # TODO - potentially need a different percentage based on laser and photores being used
print("Target Goal Lighting: ", target_reading)

# Initialize LEDs to on at beginning
# These LEDs indicate lives remaining
led1 = Pin(16, Pin.OUT)
led1.value(1)
led1_on = True
led2 = Pin(18, Pin.OUT)
led2.value(1)
led2_on = True
led3 = Pin(19, Pin.OUT)
led3.value(1)
led3_on = True
lives_left = True

laser = Pin(20, Pin.OUT)
laser.value(0)

button = Pin(17, Pin.IN, Pin.PULL_DOWN)

# Initialize Score and Display
display = tm1637.TM1637(clk=Pin(1), dio=Pin(0))
score = 0
display.number(score)

# Initialize Servo
sg90.servo_pin(15)
SMOOTH_TIME = 80
servo_speed = 1

# flag so the laser can interrupt the scan cycle
kill_flag = False

# debounce utime saying wait 5 seconds between button presses
DEBOUNCE_utime = 5000

# debounce counter is our counter from the last button press
# initialize to current utime
debounce_counter = utime.ticks_ms()
       
def scan(servo):
    stepping = servo_speed
    for i in range(45,130, stepping):
        if (kill_flag):
            break
        servo.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(130,45, -stepping):
        if (kill_flag):
            break
        servo.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)
        
# define a function to execute in the second thread
def second_thread_func():
    while True:
        # fix for import failing in second thread when it's inside a function
        servo = sg90
        stepping = servo_speed
        scan(servo)
        #print("servo_speed=", servo_speed)
        utime.sleep_ms(100)

# Start the second thread
_thread.start_new_thread(second_thread_func,())

# Function to handle darkening one LED
def remove_led():
    global led3_on, led3, led2_on, led2, led1_on, led1, lives_left
    if(led3_on):
      led3.value(0)
      led3_on = False
    else:
        if(led2_on):
          led2.value(0)
          led2_on = False
        else:
            led1.value(0)
            led1_on = False
            lives_left = False
            end_of_game_buzz()
            
# Function to handle when the button is pressed
def button_press_detected():
    global debounce_counter
    current_utime = utime.ticks_ms()
    
    # Calculate utime passed since last button press
    utime_passed = utime.ticks_diff(current_utime,debounce_counter)

    # print("utime passed=" + str(utime_passed))
    if (utime_passed > DEBOUNCE_utime):
        print("Button Pressed!")
        # set debounce_counter to current utime
        debounce_counter = utime.ticks_ms()

        fire_the_laser()    
    #else:
        #print("Not enough utime")

def fire_the_laser():
    print("FIRE ZEE LASERS!")
    global servo_speed

    enable_laser()   
    check_target()     
    disable_laser()

    if (photo_reading > target_reading):
        its_a_hit()  
    else: 
        its_a_miss()

def enable_laser():
    global kill_flag
    kill_flag = True
    laser.value(1) 
    utime.sleep_ms(2000) 

def disable_laser():
    global kill_flag
    utime.sleep_ms(1000)   
    kill_flag = False
    laser.value(0)

def check_target():
    global photo_reading
    photo_reading = photoresistor_value.read_u16()   
    print("Laser Voltage Reading: ",photo_reading)

def increase_difficulty():
    global servo_speed
    servo_speed = servo_speed + 1

def increase_score():
    global score
    score = score + 1

def display_score():
    display.number(score)

def its_a_hit():
    print("Nice! - A Hit!")
    happy_buzz()
    increase_difficulty()
    increase_score()
    display_score()
    print("Score: ", score)

def its_a_miss():
    print("Ouch - A Miss!")
    sad_buzz()
    remove_led()

def happy_buzz():
    print("Time to get buzzed!") # TODO - this method

def sad_buzz():
    print("Time to get buzzed!") # TODO - this method

def end_of_game_buzz():
    print("Time to get buzzed!") # TODO - this method

# Below executes in the main(first) thread.
while True:
    if (lives_left):
      if button.value()==True:
        button_press_detected()
    else:
        print("Game Over!")
        kill_flag = True
        laser.value(1)
        sys.exit()
