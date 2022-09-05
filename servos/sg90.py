## according to this: https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/
## The duty cycle maxes at 65535 for the
## Raspberry Pi Pico has 12 bit resolution but in MicroPython it is scaled to 16 bits.
## Hence the duty cycle is set from 0-65535 which corresponds to 0-100%. (min duty cycle for Pico to Max duty cycle for Pico)
## However, for SG-90 servo motor we will pass values between 1000-9000 microseconds
## which corresponds to 0-180 degree position movement of the arm inside the PWM.duty_u16() method.

## Barry's notes:  But this calculation seems to indicate max duty cycle for SG90 is actually 8,191.875, not 9000
## This method takes the SG90 calculated pulse width in ms and converts it to the right duty cycle
def _calc_duty_cycle(pulse_width):
    return (pulse_width) * (65535) / (20)

## according to this: https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/
## Position 1000 to 9000 represents 0 to 180
## Specs on SG90 servo say Pulse Width of 0.5 is 0 and 1.5ms is mid point and 2.5ms is max.
## This formula works to get the pulse width for the sg90 servo based on the angle.
def _calc_pulse_width(angle):
    return (angle * 2.0) / 180 + 0.5


def duty_cycle_for_angle(angle):
    print("===== New Write ==== ")
    print("angle=" + str(angle))
    # pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    pulse_width=_calc_pulse_width(angle)
    #duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    duty=int(_calc_duty_cycle(pulse_width))
    print("pulse width=" + str(pulse_width))
    print("duty=" + str(duty))
    
    return duty


