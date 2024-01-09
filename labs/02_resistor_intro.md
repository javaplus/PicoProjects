# Resistors

## Overview

From the previous lab, you should see your Blue LED is very bright.  We know that we are getting power from the 3.3V pin from Pico.  But what we didn't talk about was the voltage rating of the LED.  Let's look at the Voltage rating and other specifications for the LEDs in our kit:

##### LED Specification Table
![LED Specs](/images/LED_SPECS.PNG)


Our LED's (like most electronics) have voltage ranges in which they are designed to run.  As mentioned above, we are currently running off 3.3Volts, but if we look again at the specifciations for the LEDs, we will see we are actually running a little over the specified voltage range of 3.0 to 3.2V for our Blue LED.  This is why it's so bright.  It's running slightly above max power!

Notice that the WHITE, BLUE, and GREEN LEDS support up to 3.2Volts. The other LEDs (RED and YELLOW) only support upto 2.2Volts.  So, if we tried to use a Red or Yellow LED with our current circuit we could burn them out.

Since we are barely over spec with our Blue LED we most likely won't have an issue, but it would be safer for the lifespan of the LED to run at a lower voltage. 


## Resistors

 One simple way to lower the voltage in a circuit is to use a resistor.  A resistor simply resists(or restricts) the flow of electricity.  So, by adding a resistor into our circuit we will drop our voltage to a safer level.  

 Resistance is measured in Ohms.  The higher the Ohms the more resistance.  You should have at least 2 resistors in your kit.  We will try them both to determine which has the most resistance.

 Resistors as seen in the image below have two legs. These legs are not polarized... meaning it doesn't matter which leg plugs into what part of the circuit.  as long as the legs are used to complete a circuit, the body in the middle will resist the flow of electron flow.

###### Resistor
![Resistor image](/images/resistor.png)



 ## What to do

For our simple LED circuit it doesn't matter if we add the resistor to the positive side or the negative side because it will restrict the flow for the whole circuit.  However, we will simply replace our Red wire connecting the long leg of the LED to the positive rail with a resistor.  

So, remove the red wire connecting the positve rail to Pin 30 (long side of the LED). Replace that wire with one of the resistors in your kit.  It doesn't matter which resisitor at this point.  

Once you connect the resistor, you should see the LED light up again, but be dimmer.  
Swap out the resistor with another one in your kit and see if it gets even dimmer or brighter.  Can you tell by the brightness level which resistor has the most resistance(more Ohms)?

If it works pat yourself on the back.

### More Information

While we tried to figure out which resistor had more resistance by just trying it in a circuit with an LED, it's typically required to KNOW the amount of resistance needed in your circuit and then choose the correct resistor. If you don't know the value of a resistor, you can use a Volt Meter set to the Ohms setting to test.  This is the easiest way.  You can also use the color bands on the resistors to determine the resistance level. This can be complicated as some colors are hard to distinguish, but there is a neat resistor calculator that allows you to enter the color bands to tell you the resistance: [Resistor Calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code) 
![Resistor Circuit](/images/2_Circuit_bb.png)
