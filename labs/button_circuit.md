# Button/Switch

## Overview

Now we will show how to use a simple button or momentary switch to keep the circuit open until you press the button.  So, when you finish this lab, the LED should only light up when you hold in the button.

## How a Switch Works

A button or switch is simply a way to close a circuit (allow electricity to flow) with a mechanical device.  The easiest way to think of a button or switch is just a piece of metal that connects two leads.  See the picture below:

##### Open Circuit Image
![Switch Circuit Off](/images/switch_circuit.png)

In the circuit above, you see the switch is just a metal bar that in it's current state would not allow the electrcity to flow.  The blue wire from the battery pack connects to one side of the metal switch, but while it's up, the current cannot flow to the blue wire on the other side. But if the bar was pushed down(as in the picture below) it would connect the two blue wires which would close or complete the circuit and allow electricity to flow and the light would light up.
##### Closed Circuit Image
![Switch Circuit On](/images/switch_circuit_on.png)

## Our Buttons

The buttons we are using for this lab are called momentary switches or push buttons or some combination of those terms.

![Button image](/images/button.jpg)

The idea is that if you connect power to one side of the button and then the otherside connects to the rest of your circuit then electricity can only flow while you press the button down.


 ## What to do

For this lab, we will replace the potentiometer with a button.  You will no longer have resistance so your light will be super bright, but only while you press the button down.  

Remove the black ground wire that was connecting your potentiometer to the ground/negative rail and remove the Potentiometer altogether.

Take your button and place the two right side pins into column 25.  To determine left and right of the button hold the slot on the bottom side of the button vertically. 
##### Bottom view of button
![Button Slot](/images/button_bottom.jpg)

The slot on the bottom of the button separates the two sides.  So, just be sure the slot is in the same direction as the columns (vertical in the diagram below).

Now move the wire connecting to the long leg of your LED to connect to column 25.  The power rail should be connected to the left side of the button.

Now if you press and hold the button your LED should light up.

If it works think a happy thought.


![Button Circuit Diagram](/images/5_button_bb.png)