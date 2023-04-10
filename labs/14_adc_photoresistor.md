# Reading Analog Inputs

## Overview

Now we are going to switch gears and go back to working with our Photoresistor (or light-dependent resistor). So, far the only input we've worked with in our code on the Pico is with our button.  A button is a simple binary type of input.  That is it only has two states; it's either on or it's off.  However, a lot of sensors, like our Photoresistor, are analog and not binary.  Analog meaning there's a range of values that it can produce instead of a simple on or off.


## Working with Analog inputs 

To work with analog sensors on the Pico, we will need to use the Analog to Digital specific pins on the Pico.  This is because internally the Pico deals with digital signals; therefore, to work with analong inputs, the Pico has to translate the analog signals to digital through an aptly named Analog-to-Digital Convertor(ADC).  Luckily an Analog-to-Digital convertor is built into the Pico(unlike the normal RaspberryPi's).  There are 3 pins that give access to the ADC on the Pico. See the image below to identify the ADC GPIO pins:

![ADC GPIO Pins](/images/adcpins.PNG)


 ## What to do

We will now plug our Photoresistor back into the board and write some code to read values that will vary based on the amount of light hitting our light-dependent resistor.  

You can skip to the wiring diagram below and just follow it, but below is more descriptive instructions.

Clear the board except for the wires connecting to the power rails.
Then add the photoresistor with one leg into column 35 and the other leg in column 38.  Connect the leg of the photoresistor in column 38 to the 3.3v power rail.

Now connect the leg of the photoresistor in column 35(left leg) to the pin on the Pico in Column 7, Row I or J (this is our ADC pin).  Now connect that same leg of the photoresistor in column 35 to ground with a 10K resistor.

Resistors are identified by the pattern of their color bands, some have 4 bands and others have 5. For 10k resistors:
| 4 Band Color Pattern | 5 Band Color Pattern |
| --- | --- |
| Brown-Black-Orange-Gold | Brown-Black-Black-Red-Gold |

<details>
<summary> Want to read why need the 10K resistor, expand this.</summary>
The 10K resistor is needed to create what's called a <a href="https://learn.sparkfun.com/tutorials/voltage-dividers">voltage divider</a>.  I'd like to explain exactly what that means, but I can't... I'm an electronics noob.  But I think the way it works is that the voltage divider causes a disturbance in the force by disrupting the <a href="https://starwars.fandom.com/wiki/Midi-chlorian">midi-chlorian</a> flow and therefore causes the <a href="https://www.dictionary.com/e/fictional-characters/flux-capacitor/">flux capacitor</a> to emit a lesser charge through the <a href="https://ghostbusters.fandom.com/wiki/Proton_Pack">proton pack</a> than it normally would. If you are more confused after reading my  nonsensical description, then you understand as much about voltage dividers as I do.  <br><b>Seriously though, the 10K resistor in parallel with the photoresistor allows us to get a wide range of values when reading the resistance.</b> Here's a good article that goes into more detail: <a href="https://learn.sparkfun.com/tutorials/voltage-dividers">Spark Fun Voltage Dividers</a>
</details>
  
  


###### Wiring Diagram
![Servo Diagram](/images/13_adc_photoresistor_bb.png)


Once everything is wired, we will write the code to work with GPIO pin #28 and configure it as an ADC input.  We will read the values from it and use a simple formula to convert that to a volage reading.  

You can copy the simple code below to display the values read from the photoresistor.

Here's the code:

``` Python
from machine import Pin, ADC
import utime
 
photoresistor_value = machine.ADC(28)
conversion_factor = 3.3/(65535)

while True:
    photo_reading = photoresistor_value.read_u16() * conversion_factor     
    print("Voltage Reading: ",photo_reading)
    utime.sleep(0.2)    
```

The ADC class from the machine library makes is super simple to work with analong input.  The **conversion_factor** allows us to take the raw 16bit integer value read from the photoresistor and change it into a voltage reading.  Recall we are working with 3.3Volts.  So, what we end up is seeing the voltage reading of the circuit. The more light the less resistance and the higher the reading.  Less light means more resistance and therefore lower voltage.

Run the code and watch the values in the terminal change as you change the amount of light hitting the resistor. Try covering it up and shining your phone's light on it.


## Optional Stretch goal

There's no code given for this stretch goal.  But if you'd like to have some fun, use the value read from the photoresistor to control the brightness of an LED.

Use PWM to make the LED get brighter as more light enters the photoresistor and make the LED get dimmer when there's less light hitting the photoresistor.


## References:

[Voltage Divider Explanation](https://learn.sparkfun.com/tutorials/voltage-dividers)

[Pico ADC Explanation and Tutorial](https://microcontrollerslab.com/raspberry-pi-pico-adc-tutorial/)
