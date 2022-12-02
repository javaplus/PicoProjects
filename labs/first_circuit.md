# Creating Your First Circuit

To create your first circuit, we first want to understand what a circuit is.  A circuit is just path for electricity to flow.  
In a typical circuit, electricity flows from a battery or some power source through wires and into something that converts electricity to some other form of energy.

The first circuit we will build will be to power a simple light (LED).

![Basic Circuit](/images/Circuit.png)

An important part of a working circuit is to make sure the circuit is complete or closed.  That is that there is a connection from the battery or power sources positive terminal through the light and to the ground(negative).  Electricity flows from the positve terminal to the ground(negative) and if there is a break or disconnect in the circuit then the circuit is "open" and therefore no electrcity is flowing and your light won't shine.

## What we will build

The first circuit is to simply power an LED.  A LED is a Light Emitting Diode.  A Diode only allows electricity to flow in one direction.  So, there is a positive and negative side to the LED.  Typically the longer leg of the LED is the positive side.


So, we will simply hook our power source to our bread board and then connect the power to the LED in the appropriate way.  See the Diagram below.

## LED Selection

We wil be connecting the 3.3Volts out pin from the Pico to the + power rail of the bread board.  Since we are using 3.3 Volts of power be sure to chose an LED with the highest voltage rating.  See the table below for your LED voltage ratings.  Notice that the WHITE, BLUE, and GREEN LEDS support upto 3.2Volts. The other LEDs (RED and YELLOW) only support upto 2.2Volts.  So, you need to use a WHITE, BLUE, or GREEN led for this exercise, otherwise you can burn out the LED.

##### LED Specification Table
![LED Specs](/images/LED_SPECS.PNG)


## What to do:

We will now connect the power rails of the breadboard to the Raspberry Pi Pico.  

##### Orientation

It will be easiest if you orient your breadboard as seen below in the wiring diagram.  The USB connection should be to the left and on the left edge of the breadboard you should see letters A through J going from the bottom up.  Across the breadboard left to right you should see numbers indicating the columns of pins starting at 1 and then counting by 5's across the board.

##### Ground (negative)

As mentioned above we a completed circuit needs to go from a positive power source to a negative or ground terminal.  So, we are going to use the Pico's power out (positive) and it's ground to be our power source.  We will start by connecting one of the ground pins on the Pico to the top ground(-) rail of the breadboard.  To do this run a black wire from Pin 3 in Row I or J to the negative rail(ground) on the bread board.  

##### Positive(positive)
Now to connect the positive side of the power rail, run a red wire from Pin 5 Row I or J to the top positive(red) rail.  Pin 5 on the Pico here is a 3.3Volt output pin.  So, if the Pico is powered up it will be producing 3.3Volts of power.

NOTE: Technically the color of wires don't matter (internally they are the same), but the color does make it easier to know the purpose.  Usually, red wires indicate positive(+) and black wires indicate ground/negative(-).  On the breadboard, the blue line represents the ground/negative power strip and the red/pink line indicates the positive side.

##### LED

Now take your BLUE LED and connect it to the breadboard plugging the slightly longer leg into Pin 30 and the shorter leg into Pin 31 (preferably in Row F)

Now run a red wire from Pin 30 (any Row G-J) to the positive power rail at the top.  Now connect the shorter leg of the LED to ground, by running a black wire from Pin 31 (any Row G-J) to the top Ground(negative) rail.

Once everything is wired, if you plug in your Pico via the USB cable, you should see the LED light up.

When you have light, rejoice! You've just made the world a little brighter literally! :)

## Wiring Diagram

![Basic LED Wiring Diagram](/images/1_Circuit_bb.png)



### Resources:

[In depth How a Breadboard Works](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all)
