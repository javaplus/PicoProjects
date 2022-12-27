from machine import Pin,PWM
import utime
import _thread
import sg90

button = Pin(17, Pin.IN, Pin.PULL_DOWN) # potential TODO - change PIN of button
# debounce utime saying wait 3 seconds between button presses
DEBOUNCE_utime = 3000

# debounce counter is our counter from the last button press
# initialize to current utime
debounce_counter = utime.ticks_ms()

# Initialize LASER
laser = Pin(16, Pin.OUT)

photoresistor_value = machine.ADC(28)  # potential TODO - change PIN of photores
conversion_factor = 3.3/(65535)


laser.value(0)
firing_flag = False
firing_start_time = 0

# Initiliaze Servo
sg90.servo_pin(15)
SMOOTH_TIME = 20
servo_speed = 1
score = 0

lives_left = True

def its_a_hit():
    # TODO - happy buzzer buzz
    global servo_speed, score
    print("HIT!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    servo_speed = servo_speed + 1
    score = score + 1
    #display.number(score)
 
def its_a_miss():
    # TODO - sad buzzer buzz
    #remove_led()
    print("Missed!")

def get_target_value():
    photo_reading = photoresistor_value.read_u16() * conversion_factor
    return photo_reading

def check_target_hit(photo_reading, initial_photo_reading):
    variance = 1      # TODO - figure out proper variance for shot logic
    
    if (photo_reading > (initial_photo_reading + variance)):
      its_a_hit()
    else: 
      its_a_miss()
    

# Function to handle when the button is pressed
def button_press_detected():
    global debounce_counter, firing_flag, firing_start_time
    current_utime = utime.ticks_ms()
    # Calculate utime passed since last button press
    utime_passed = utime.ticks_diff(current_utime,debounce_counter)
    #print("utime passed=" + str(utime_passed))
    if (utime_passed > DEBOUNCE_utime):
        print("Button Pressed!")
        # set debounce_counter to current utime
        debounce_counter = utime.ticks_ms()
        
        laser.value(1)  # TODO - no idea if this logic is right for firing the laser
        firing_flag = True
        firing_start_time = utime.ticks_ms()

    #else:
     #   print("Not enough utime")

       
def scan(servo):
    stepping = servo_speed
    for i in range(90,130, stepping):
        servo.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(130,89, -stepping):
        servo.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)


    for i in range(90,45,-stepping):
        servo.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(45,91, stepping):
        servo.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)
        

# define a function to execute in the second thread
def second_thread_func():
    while True:
        # fix for import failing in second thread when it's inside a function
        servo = sg90
        stepping = servo_speed
        scan(servo)
        print("servo_speed=", servo_speed)
        utime.sleep_ms(100)

# Start the second thread
_thread.start_new_thread(second_thread_func,())

# every 5 second increase servo speed
last_time_checked = utime.ticks_ms()
def set_servo_speed():
    global last_time_checked
    diff_time = utime.ticks_diff(utime.ticks_ms(), last_time_checked)
    if(diff_time > 5000):
        last_time_checked = utime.ticks_ms()
        return (servo_speed + 1)
    else:
        return servo_speed

current_target_value = 0
highest_target_value = 0
firing_time_ms = 0
firing_time_limit_ms = 500
## get initial value from target
initial_photo_reading = get_target_value()
utime.sleep_ms(1000)
print("Initial Voltage Reading: ",initial_photo_reading)

# Below executes in the main(first) thread.

try:
    
    while True:
        if (lives_left):
          if button.value()==True:
            button_press_detected()
          if(firing_flag == True):
              firing_time_ms = utime.ticks_ms() - firing_start_time
              current_target_value = get_target_value()
              if(current_target_value > highest_target_value):
                  highest_target_value = current_target_value
                  #print("firing_time=",firing_time_ms)
              if(firing_time_ms > firing_time_limit_ms):
                  print("highest target value=", highest_target_value) 
                  firing_flag = False
                  firing_time_ms = 0
                  laser.value(0)
                  check_target_hit(highest_target_value, initial_photo_reading)
                  highest_target_value = 0
              
        else:
            print("YOu dead")
except Exception as e:
    ## TODO Handle exception
    print("Exception",e)
except KeyboardInterrupt as ki:
    ## TODO Handle exception (kill second thread)
    print("keyboard Interrupt", ki)


