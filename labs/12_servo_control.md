# SERVO MOTORS!!

## Overview

We will now finally do something completely different! No more just flashing LEDs!  Now we will use a [Servo](https://www.sparkfun.com/servos) to turn code into physical movement.  


## What's a Servo?

###### Sg90 Servo
![Servo Image](/images/sg90.png)

A **Servo** is typically just a simple motor with internal gears and a built-in controller that allows you to tell it what position to move to and hold.  Servos are commonly used in robotics as well as R/C planes and cars.  Most servos are designed to be controlled by a PWM signal which is like a digital code to say what angle or position to rotate to.  

## How they Work

Servos typically have 3 wires.  Two are for power (positive and negative(ground)) and then the third is the signal wire which takes the PWM signal.  
![Servo Wires](/images/sg90_wires.PNG)

Red wire goes to Positive,  brown wire goes to ground/negative, and the Orange wire is the PWM signal wire.  

To control a servo, the duty cycle of the PWM signal acts as the digital code telling on the servos controller where to move or hold the motor.
 <details>
 <summary>Expand to read boring technical stuff about PWM and Servo control!</summary>
Servos are designed to work at a specific frequency (50Hz) and use the duty cycle of the PWM signal to control the movemnt of the servo.  
Technically, for most servos, the pulse width (time the power is on in a pulse) matters more than the duty cycle(the % of time power is on), but at a given frequency the duty cycle directly controls the pulse width.
</details>
  
 ## What to do

Upto this point everything we've been using is running of the Pico's 3.3Volt output.  For this lab, we will use the Pico's 5Volt output.

Clear the board of LED's and buttons and extra wires.  You can leave the power rail wires that connect to the top power rail.  We won't use the top power rail, but it doesn't hurt to leave them connected.

With the board clear, grab a red wire and connect it from the Pico  5 Volt power (VBUS) to the bottom positive rail.  The Pico's **VBUS** is a 5 volt out and it's connected to the top column 1.  So, connect your red wire to column 1 row j and then to the bottom positve rail as seen in the diagram below.

Connect a black wire from one of the Pico's bottm ground pins to the bottom negative rail.  The bottom two pins in column 3 are a good choice.

With the bottom power rails connected to the Pico, now wire up the servo.  Use a male to male wire to connect the brown servo wire to the ground rail(negative) on the breadboard.  
Use a wire to connect the servo's red wire to the bottom positive rail.

Use another wire to connnect the servo's yellow wire to GPIO 15 on the Pico which can be found in column 20 at the bottom( orange wire connected to column 20, Row B in the picture below).

![Servo Diagram](/images/12_servo_pico_bb.png)


Once you have the pico wired, we need to write the code to control the servo.

To begin with our code will simply move the servo to the center, then rotate 90 degrees in one direction and the rotate to the opposite extreme (180 degrees in the opposite direction).

To make your code with the servo simple, I've created a library that you can simply copy to your pico and import into your program.

Right click on the link below to open the SG90 library in another tab.  Then copy it and paste it into a new file in Thonny (CTRL + N is the keyboard shortcut). After copying it into Thonny save it to the Pico and be sure to name it **"sg90.py**.
[SG90 Library](https://raw.githubusercontent.com/javaplus/PicoProjects/main/servos/sg90.py)


Once you have the **sg90.py** library saved to your Pico, open a new file/tab (CTRL + N) in Thonny and add the following code.

Here's the code:

``` Python
import sg90
import utime

# initialize the signal Pin
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
    
```

Before running the code above, you may want to snap one of the servo horns ontop of the servo so you can see it's movement.
###### Servo Horn
![Servo Horns](/images/sg90-servo-horns.png)
It doesn't matter which servo horn you use, just snap one on so you can more easily see when it moves.

After you have the code and servo horn in place, click the PLAY button to see your servo spring to life!

If everything is working right, then your servo should center itself and then move to one extreme 90 degrees and then move the opposite direction 180 degrees and then move back to its center position.

## Scanning

Now that you have a simple program that shows how to set the angle of the servo, let's make it more intersting by adding some for loops to make it slowly scan back and forth.

By the code above, you can see you set the angle you want the servo to move to.  The library translates that to a specific duty_cycle to send out your signal pin.
If you loop and slowly increase or decrease the angle, then you should see the servo move or "scan" in that one direction.

The servos we are working with can move from 0 to 180 degrees.  So, valid input are anything in that range.  90 degrees is the center.  So, add a for loop or a few to start at 90 and then slowly scan to 180 and then go back the other direction.

You will want to use a for loop. Here's Python for loop help: [Python For Loop with Range](https://www.w3schools.com/python/gloss_python_for_range.asp)

<details>
 <summary>To see working code for this click the arrow beside here to expand the code!</summary>
  

```Python
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

    
```

</details>

If you got this to work, scan the room for someone cool, when found go to them and say, "Hey your smoother than zero duty cycle!"

## References:

[Servo Explained](https://www.sparkfun.com/servos)
[SG90 Specs](https://servodatabase.com/servo/towerpro/sg90)
[Pico PWM Primer](https://www.codrey.com/raspberry-pi/raspberry-pi-pico-pwm-primer/)
