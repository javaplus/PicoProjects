# Pico Projects

This is our amazing introduction to basic electronics and working with the Raspberry Pi Pico microcontroller.  These lessons will help you bring code to life and release your inner mad scientist!

## Prerequisites

Basically you just need the simple Python editor called Thonny which allows you write code on your laptop and execute it on the Pico via a USB cable. USB cables will be provided just make sure you have a laptop with Thonny installed and an available USB jack on your laptop.  We will have a few USB C to USB A adapters for those with only tiny ports. We will not have Mac dongles so make sure you have a way to connect a USB A cable into your laptop. 

Please download and install the latest version(4.x or higher) of Thonny.  
[Download Thonny](https://thonny.org/) 

For these labs, you do NOT have to be a Python expert.  You can probably get by fine without having ever done Python programming before.  However, some general programming knowledge is required. As long as you are comfortable with basic programming constructs(IF/ELSE statements, For/While loops, etc...) in other languagues we will have enough of the code for you to figure out the Python bits.
If you want to get a little familar with Python before coming you can check out this free tutorial get comfortable with Python. We will have code samples and links to reference materials if you just need to see how to do "normal" programming things in Python.
[Python Tutorial](https://www.learnpython.org/)


## Are you Running a Hackathon

If you are using this as part of a Hackathon or contest, check out our [Hackathon Guide](/reference/hackathon.md).

## Overview 

We start with a basic introduction to circuits and some basic electronics. So, the first several labs only use the Pico as a power source to introduce basic circuits and some electronic components we will be working with.  Without this foundational knowledge, it will be difficult to build useful solutions that integrate code and electronics.

If you aren't familar with how to use a breadboard, please take a moment and look at our introduction to them before starting the labs: [Introduction to Breadboards](/reference/breadboards.md)

**NOTE on LABS**  
We provide working code for each lab, but you are welcome to try to code some of the stretch goals or solutions on your own once you get the hang of things.  

Many of the labs reference specific columns and rows to use when plugging in electronics.  This is just to make it easier for beginners.  The exact column and rows do not matter if you already understand how a breadboard works and know how to complete the circuit.  If this is all brand new to this, you should follow our instructions exactly. But just know as you learn more about breadboards and circuits the exact location you plug things into the breadboard in many of the labs aren't important if you still complete the circuit.

If you finish a lab quickly and see others that are struggling, **your stretch goal is to help a neighbor!**

## Optional Path

Instead of going sequentially through the labs, you can instead use the [Parts Description](https://github.com/javaplus/PicoProjects/blob/main/reference/part_description.md) page to see a list of all the cool gadgets you can use to build a game and then choose your own adventure.

## Intro to Circuits.

Simple circuit with LED using power from Pico and turn on LED.   
[Lab 1](/labs/01_first_circuit.md)

## Resistors.

Same simple circuit from above and just add resistors to control the brightness of the LED.  
[Lab 2](/labs/02_resistor_intro.md)

## Variable Resistors (Photoresistor)

Working with Light Sensitive Resistors. Also known as Photoresistors.  
[Lab 3](/labs/03_photo_resistor.md)

## Variable Resistor (Potentiometer)

Use a Potentiometer to control brightness of LED.  
[Lab 4](/labs/04_potentiometer.md)

## Buttons/Switches

Introduction to using Buttons/Switches with cicuits:  
[Lab 5](/labs/05_button_circuit.md)

## Use Code to Flash LED (First Lab with Pico and MicroPython)

Finally, we will use code to light up LEDs:   
[Lab 6](/labs/06_blink_yo_self.md)  
[Lab 7](/labs/07_blink_led.md)  
 

## Working with Buttons and the Pico

Use the Pico to detect when a button is pressed.  
[Lab 8](/labs/08_button_control.md)  
[Lab 9](/labs/09_button_debounce.md)  
[Optional Game - Reaction Time Lab 16](/labs/16_button_led_reaction_time.md)  
[Lab 10](/labs/10_button_interrupt.md)  



## Pulse Width Modulation (PWM)

Explain PWM and use PWM to fade an LED in and out and control brightness.  
[Lab 11](/labs/11_PWM_LED.md)

Buzzer lab with PWM.  
[Lab 11b](/labs/11b_Buzzer.md)

## PWM to Control Servos

Use PWM to control a servo:  
[Lab 12](/labs/12_servo_control.md) 

## Joystick and Turrets(Optional)
[Joystick Lab](/labs/Joystick_intro.md)  
[Turret Lab](/labs/turret.md)

## Threading in MicroPython

Threading on the Pico:  
[Lab 13](/labs/13_threading.md) 


## Reading PhotoResistor Values

Using Analog input with the Pico:  
[Lab 14](/labs/14_adc_photoresistor.md)

## Seven Segment Display

Seven Segment Display:  
[Lab 15](/labs/15_seven_segment.md) 


## Build the Laser Shooting Shark Game:
[Final Lab 01](/labs/f01_fire_zee_lasers.md)  
[Final Lab 02](/labs/f02_sharks_with_lasers.md)  
[Final Lab 03](/labs/f03_grand_finale.md)  



## References:
  #### Parts List
  - Pico, Pico H, or Pico W (Pico H is less work since it has pins soldered already)
  - Breadboard
  - Jumper Wires
  - LEDs
  - Button (push button switch)
  - micro USB cable
  - Active Buzzer
  - Photoresistor(5528, but others would work)
  - Resistors(220 Ohm, 10K Ohm) 2 of each
  - sg90 type mini servo
  - 10K Ohm Trim Potentiometer
  - 3D printed parts for final 3 game labs & paint stirring stick.[Models](https://github.com/javaplus/PicoProjects/tree/main/models)

[Spreadsheet with Links where I ordered most parts](https://docs.google.com/spreadsheets/d/19XlUfh7XKboxZuTpR78YdXvtKbAR8O2FZtGRgrgSMsw/edit?usp=sharing)

  #### Python:
  - [While loops](https://www.geeksforgeeks.org/python-while-loop/)
  - [for loops](https://www.geeksforgeeks.org/python-for-loops/)
  - [if statements](https://www.geeksforgeeks.org/python3-if-if-else-nested-if-if-elif-statements/)
  - [time calculations/deltas](https://docs.micropython.org/en/latest/library/time.html#time.ticks_diff)
 
#### Pico:

- [Pico GPIO Pinout](/reference/pico_gpio.md)

- [MicroPython RP Pico Library](https://docs.micropython.org/en/latest/rp2/quickref.html)  
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
## 
