import machine
class servo:

    DEBUG = False
        
    def __init__(self, pin):
        self.servo = machine.PWM(machine.Pin(pin))
        self.servo.freq(50)
        self.position = 90 #new
        self.move_to(self.position) #new
    
    ## Barry's notes:  But this calculation seems to indicate max duty cycle for SG90 is actually 8,191.875, not 9000
    ## This method takes the SG90 calculated pulse width in ms and converts it to the right duty cycle
    def __calc_duty_cycle(self, pulse_width):
        return (pulse_width) * (65535) / (20)

    ## according to this: https://microcontrollerslab.com/servo-motor-raspberry-pi-pico-micropython/
    ## Position 1000 to 9000 represents 0 to 180
    ## Specs on SG90 servo say Pulse Width of 0.5 is 0 and 1.5ms is mid point and 2.5ms is max.
    ## This formula works to get the pulse width for the sg90 servo based on the angle.
    def __calc_pulse_width(self, angle):
        return (angle * 2.0) / 180 + 0.5


    def duty_cycle_for_angle(self, angle):
        if self.DEBUG:
            print("===== Calcing Duty Cycle for Angle ==== ")
            print("angle=" + str(angle))
        # pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
        pulse_width=self.__calc_pulse_width(angle)
        #duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
        duty=int(self.__calc_duty_cycle(pulse_width))
        if self.DEBUG:
            print("pulse width=" + str(pulse_width))
            print("duty=" + str(duty))
        
        return duty
    def move_to(self, angle):
        duty_cycle=self.duty_cycle_for_angle(angle)
        self.servo.duty_u16(duty_cycle)
        self.position = angle #new
