# Pico Projects

This is our amazing introduction to basic electronics and working with the Raspberry Pi Pico microcontroller.  These lessons will help you bring code to life and release your inner mad scientist!

## Prerequisites

Basically you just need the simple Python editor called Thonny which allows you write code on your laptop and execute it on the Pico via a USB cable. USB cables will be provided just make sure you have a laptop with Thonny installed and an available USB jack on your laptop.  We will have a few USB C to USB A adapters for those with only tiny ports. We will not have Mac dongles so make sure you have a way to connect a USB A cable into your laptop. 

Please download and install the latest version(4.x or higher) of Thonny.  
[Download Thonny](https://thonny.org/) 

For these labs, you do NOT have to be a Python expert.  You can probably get by fine without having ever done Python programming before.  However, some general programming knowledge is required. As long as you are comfortable with basic programming constructs(IF/ELSE statements, For/While loops, etc...) in other languagues we will have enough of the code for you to figure out the Python bits.
If you want to get a little familar with Python before coming you can check out this free tutorial get comfortable with Python. We will have code samples and links to reference materials if you just need to see how to do "normal" programming things in Python.
[Python Tutorial](https://www.learnpython.org/)


## Overview (Work in progress Below)

We start with a basic introduction to circuits and some basic electronics.  Without this foundational knowledge, it will be difficult to build useful solutions that integrate code and electronics.

[Lab 1](/labs/first_circuit.md)

## Intro to Circuits.

Simple circuit with LED using power from Pico and turn on LED. 
- Use 3.3v from Pico and Blue LED to support Voltage.

## Resistors.

Same simple circuit from above and just add resistors to control the brightness of the LED.

## Variable Resistors (Photoresistor)

Replace resistor with photo resistor and see LED dim and brighten based on light going into photoresisotor

## Variable Resistor Potentiometer

Replace Photo resistor with Potentiometer to control brightness of LED

## Buttons/Switches

Go back to normal resistor and then add a button in the circuit so that the LED only comes on when the button is pressed.

## Control LED from Pico

Remove button and wire LED to Pico and ground.  Then write code to blink LED. Maybe blink on board LED first.
- Stretch goal: having more than one LED.

## Read input (button input)

Hook the button up to the Pico and code it so that the light comes on only when the button is pressed, but have the code detect when the button is pressed and control when the LED comes on.
- stretch goal: make it so that the LED comes on with one press of the button and stays on and then turns off with a second press of the button.
- stretch goal: hook up buzzer and have it buzz when button is pressed or create game to have button pressed within a short time after the light goes on.


## PWM with LED

Explain PWM and use PWM to fade an LED in and out and control brightness.

## PWM with Servo

Use PWM to control a servo.  Explain how PWM is the signal/code to control where a servo should move to.  Use SG90 library to control servo.  Maybe dig into the SG90 library a little more to explain PWM.
- Stretch Goal: sentry program that requires starting at 90 and then slowly panning to the right then panning back to center(90) before panning left again.



## Referenes:
  May need references for Python on how to do various things:
  - [While loops](https://www.geeksforgeeks.org/python-while-loop/)
  - [for loops](https://www.geeksforgeeks.org/python-for-loops/)
  - [if statements](https://www.geeksforgeeks.org/python3-if-if-else-nested-if-if-elif-statements/)
  - [time calculations/deltas](https://docs.micropython.org/en/latest/library/time.html#time.ticks_diff)
  - etc...

### Pico:

[MicroPython RP Pico Library](https://docs.micropython.org/en/latest/rp2/quickref.html)

## 
