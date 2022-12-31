# SERVO MOTORS!!

## Overview

Now that we know how to flash LEDs and know how to move servos, what if we wanted to do them at the same time???

In this lab we will learn how to take advantage of both cores of the RP2040 microcontroller processor by running a second thread to do some work in parallel.

The plan is to have one thread to make the servo continually scan, while the main thread blinks an LED.

Before we get to threading let's demonstrate the issue, by trying to do both things at once without threading.  That is we will attempt to move the servo back and forth and fade the LED in and out without threading.
  
 ## What to do

Keep your servo hooked up and wire your LED back up to pin 16.

Follow the diagram below to connect the blue LED positive leg to column 25 and the negative to column 26.  Then connect the positive leg to the GP16 pin on the Pico(Column 20).  Ground the other side of the LED leg.

![Servo Diagram](/images/servo_with_led_pico_bb.png)


Once you have the pico wired, we need to write the code to control the servo and fade the LED in and out.  This code should look familiar because it's pretty much the servo code from last lab along with a function to fade LED in and out added to it.

```Python
from machine import Pin,PWM
import utime
import sg90

# Initialize LED
led = PWM(Pin(16))
led.freq(500)

# Initiliaze Servo
sg90.servo_pin(15)
SMOOTH_TIME = 10

def fade_led():
    for duty in range(0,65535,1):
        led.duty_u16(duty) # 65535 is max
    for duty in range(65535,0,-1):
        led.duty_u16(duty) # 65535 is max
            
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


while True:
    scan()
    fade_led()

```

In the code above, we simply define the two functions, one for the LED fade and the other to scan/move the servo back and forth.  Then we call each of them while loop indefinitely. 

Copy and paste the code above into Thonny and run it.

You should see the servo move back and forth and then the LED fade up and then down.  But they will not happen at the same time.  Now you could do a lot of fancy coding to make this work in a single threaded way, but with the Pico, you've got two cores, so let's use them!

Now we will alter the code slightly to run the servo scan in a second thread, while the main thread handles the LED fade.

Here's the code:

``` Python
from machine import Pin,PWM
import utime
import sg90
import _thread


# Initialize LED
led = PWM(Pin(16))
led.freq(500)

# Initiliaze Servo
sg90.servo_pin(15)
SMOOTH_TIME = 10

def fade_led():
    for duty in range(0,65535,1):
        led.duty_u16(duty) # 65535 is max
    for duty in range(65535,0,-1):
        led.duty_u16(duty) # 65535 is max
        
def scan():
    for i in range(90,180):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(180,89, -1):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)


    for i in range(90,-1,-1):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(0,91):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

# define a function to execute in the second thread
def second_thread_func():
    while True:
        scan()

# Start the second thread
_thread.start_new_thread(second_thread_func,())

# Below executes in the main(first) thread.
while True:
    fade_led()
    
```

Notice in the code above, we've added an import for `_thread`. This gives us access to the [thread libraries](https://docs.python.org/3.10/library/_thread.html#module-_thread).  We then defined a new function called `second_thread_func()` to define what we want to do in our new thread, which in our case, is to loop forever while scanning.  
Then we use the `_thread` library's [start_new_thread()](https://docs.python.org/3.10/library/_thread.html#thread.start_new_thread) function to spawn a new thread and excute our function.  In the main while loop, we just execute our `fade_led()` function over and over again.

**NOTE** In Thonny when executing code with threads, it can have issues stopping both threads, so you may have to use a `CTRL + D` to do a "SOFT BOOT" to fully stop your code.  This can also be found by going to the **RUN** menu and then **Send EOF / Soft reboot** option.

Try running your new code and if you did everything right, then you should see the servo moving and the LED fading in and out at the same time.

If you got this to work, pat your head and rub your tummy at the same time!


## Sharing Data Between Threads

What if I need to pass information from one Thread to another.  Well in the full blown Python ecosystem, you'd have access the [queue](module) which is a great way of asynchronously and safely passing data between threads.  However, as of this time, this does not exist in MicroPython. So, to share data in MicroPython between running threads, I've only been able to succeed with [global variables](https://www.freecodecamp.org/news/python-global-variables-examples/). Probably not the best solution, but I can't find a better way within MicroPython.

We are going to modify the code above now to have the main thread calculate how fast the servo should be scanning by increasing the speed(actually the step) the servo uses to rotate.  
I've added a function called `set_servo_speed()` which retuns the value the servo should step at... it starts at 1 and every 5 seconds it increases it by 1.

Here's the whole code:
```Python
from machine import Pin,PWM
import utime
import sg90
import _thread


# Initialize LED
led = PWM(Pin(16))
led.freq(500)

# Initiliaze Servo
sg90.servo_pin(15)
SMOOTH_TIME = 20
servo_speed = 1

def fade_led():
    for duty in range(0,65535,1):
        led.duty_u16(duty) # 65535 is max
    for duty in range(65535,0,-1):
        led.duty_u16(duty) # 65535 is max
        
def scan():
    stepping = servo_speed
    for i in range(90,180, stepping):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(180,89, -stepping):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)


    for i in range(90,-1,-stepping):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)

    for i in range(0,91, stepping):
        sg90.move_to(i)
        utime.sleep_ms(SMOOTH_TIME)
        

# define a function to execute in the second thread
def second_thread_func():
    while True:
        scan()
        print("servo_speed=", servo_speed)
        utime.sleep_ms(2000)
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
    
# Below executes in the main(first) thread.
while True:
    fade_led()
    servo_speed = set_servo_speed()

```

Notice now the `scan()` function uses the global variable called `servo_speed` to set it's `stepping` variable which controls how fast the servo rotates back.

Run the code above and you should see the servo increase in movement speed every 5 seconds.  

Now this is a trivial example, but if you needed to control how fast that servo is using some input in the main thread, this is the way you could do that.
**Hint** This will be useful in the final game!

## References:

- [Threading on the Pico Tutorial](https://www.electrosoftcloud.com/en/multithreaded-script-on-raspberry-pi-pico-and-micropython/)

- [Threading MicroPython Docs](https://docs.micropython.org/en/latest/library/_thread.html)  
- [Threading Python Docs](https://docs.python.org/3.10/library/_thread.html#module-_thread)
