# Creating Your First Circuit

To create your first circuit, we first want to understand what a circuit is.  A circuit is just path for electricity to flow.  
In a typical circuit, electricity flows from a battery or some power source through wires and into something that converts electricity to some other form of energy.

The first circuit we will build will be to power a simple light (LED).

![Basic Circuit](/images/Circuit.png)

An important part of a working circuit is to make sure the circuit is complete or closed.  That is that there is a connection from the battery or power sources positive terminal through the light and to the ground(negative).  Electricity flows from the positve terminal to the ground(negative) and if there is a break or disconnect in the circuit then the circuit is "open" and therefore no electrcity is flowing and your light won't shine.

## What we will build

The first circuit is to simply power an LED.  A LED is a Light Emitting Diode.  A Diode only allows electricity to flow in one direction.  So, there is a positive and negative side to the LED.  Typically the longer leg of the LED is the positive side.

NOTE: Technically the color of wires don't matter (internally they are the same), but the color does make it easier to know the purpose.  Usually, red wires indicate positive(+) and black wires indicate ground/negative(-).  On the breadboard, the blue line represents the ground/negative power strip and the red/pink line indicates the positive side.

So, we will simply hook our power source to our bread board and then connect the power to the LED in the appropriate way.  See the Diagram below.

## LED Selection

We wil be connecting the 3.3Volts out pin from the Pico to the + power rail of the bread board.  Since we are using 3.3 Volts of power be sure to chose an LED with the highest voltage rating.  See the table below for your LED voltage ratings.  Notice that the WHITE, BLUE, and GREEN LEDS support upto 3.2Volts. The other LEDs (RED and YELLOW) only support upto 2.2Volts.  So, you need to use a WHITE, BLUE, or GREEN led for this exercise, otherwise you can burn out the LED.

##### LED Specification Table
![LED Specs](/images/LED_SPECS.PNG)

## Wiring Diagram

![Basic LED Wiring Diagram](/images/1_Circuit_bb.png)



### Resources:

[In depth How a Breadboard Works](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all)
