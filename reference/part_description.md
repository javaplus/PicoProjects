# Parts Description


## Raspberry Pi Pico

<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/pico.jpg" alt="Raspberry Pi Pico" width="120" height="100" style="border: #ffffff 6px outset;"></img></kbd>  
The Raspberry Pi Pico is a simple [microcontroller](https://www.geeksforgeeks.org/microcontroller-and-its-types) that allows the running of code to interact with many different electronic devices. This is the main part of your kit you will use for these labs to run the code to control all the different components.  You will use the [MicroPython](https://micropython.org/) programming language to write your programs to complete the labs and make your awesome creations. 
To learn more including other labs and exercises for the Pico check out the **Free Book:**[Introduction to Raspberry Pi Pico](https://hackspace.raspberrypi.com/books/micropython-pico/pdf/download)

## LED
<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/redled.webp" alt="Red LED" width="120" height="100" class="mylinky"></img></kbd>  
LEDs are the most simple components in your kit that simply turn electricity into light.  You should have access to several different colors of LEDs.  LEDs can be used to add cool colors or indicators to your projects.  
**LED Labs:** [Basic Circuit](/labs/01_first_circuit.md) : [Basic with Resistors](/labs/02_resistor_intro.md) : [With Pico](/labs/07_blink_led.md) : [Fade LED with PWM](/labs/11_PWM_LED.md)

## Laser
<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/laser-diode.png" alt="Red LED" width="120" height="100"></img></kbd>  
The Laser in the kit is just a simple LED that can focus a beam of light to a tiny spot and has more range.  It is simply a specialized LED and is controlled exactly the same way as a typical LED.  Great for pairing with a photo resistor to use as a trip wire or "shoot" a target.   
**Laser Labs** Laser is just an LED, see LED Labs. 

## Photo Resistor
<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/photeresistor.png" alt="Photo Resistor" width="120" height="100"></img></kbd>   
Photo Resistors are variable resistors that allow you to detect changes in light.  This can be used as a trip wire or target for a laser.  It can also be used to control the resistence based on light levels and could be used as a "dimmer" of sorts if used in conjunction with LEDs to adjust the brightness of LEDs based on the amount of light hitting the photo resistor.  
**Photo Resisotor Labs**: [Basic Circuit](/labs/03_photo_resistor.md) : [Reading With Pico](/labs/14_adc_photoresistor.md)

## Potentiometer
<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/trimpot.png" alt="Potentiometer" width="120" height="100"></img></kbd>  
A potentiometer is another type of variable resistor that allows you to turn a knob to adjust the amount of resistence in a circuit.  Most knobs on common electronics are actually potentiometers used to adjust things like volume, speed, frequency, etc.   
**Potentiometer Labs**: [Basic Circuit](/labs/04_potentiometer.md) : No Pico Lab with Potentiometer, but would be same as [Photo Resistor](/labs/14_adc_photoresistor.md) code wise.

## Buttons
<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/button.jpg" alt="Buttons" width="120" height="100"></img></kbd>  
A button is a simple input device that can be used for all types of applications. Through code on the Pico you can detect whether the button is pressed or unpressed.  
**Button Labs**: [Basic Circuit](/labs/05_button_circuit.md) : [Pico Basic](/labs/08_button_control.md) : [Debounce](/labs/09_button_debounce.md)  : [Mini Game](/labs/16_button_led_reaction_time.md)  :  [Interrupt](/labs/10_button_interrupt.md)  

## Servos
<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/sg90.png" alt="Servos" width="120" height="100"></img></kbd>   
Servos are simple motors that allows you to tell it a position to move to and hold. Servos are commonly used in robotics as well as R/C planes and cars. Servos are good at providing simple movement or articulation into your project.  
**Servo Labs**: [Control with Pico](/labs/12_servo_control.md) 

## Joysticks
<kbd><img src="https://camo.githubusercontent.com/900edb5945a54ebb2774a1ffae85a3404396f6cf0471a64490d7beae10ff9ec6/68747470733a2f2f6d2e6d656469612d616d617a6f6e2e636f6d2f696d616765732f492f37314b4e68784b624e424c2e5f41435f53583432355f2e6a7067" alt="Joystick" width="100" height="100"></img></kbd>   
Joysticks are a useful input device to detect movent in at least two directions.  Joysticks are great for controlling direction of servo movement or any kind of proportional movement. 
**Joystick Labs**: [Pico Basic](/labs/Joystick_intro.md)  : [Turret Lab](/labs/turret.md)
## Buzzer
<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/buzzertop.jpg" alt="Buzzer" width="100" height="100"></img></kbd>  
The buzzer is a simple output device that can make sound.  When used with PWM, you can adjust the frequency or pitch to change the sound that they make.  They are good to add an audio element to your project.  

## Seven Segment Displays
<kbd><img src="http://github.com/javaplus/PicoProjects/raw/main/images/tm1637.jpeg" alt="Seven Segment Display" width="150" height="100"></img></kbd>  
Seven segment displays are great output device to display numbers or values.  Good for showing score, lives left, or any other numeric information.  If you are creative, you can even display some words or letters.




