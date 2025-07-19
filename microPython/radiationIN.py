import machine
import utime
import _thread
import os
import random
import playRandom  # Import the sound playback module
 
#60000 kHz seems to create the most voltage
# Create PWM on GPIO 41
pwm = machine.PWM(machine.Pin(41))
pwm.freq(60000)  # Set PWM frequency to 100 kHz (5µs high, 5µs low)
pwm.duty_u16(32767)  # 50% duty cycle (range 0-65535, so 32767 is 50%)

# Set up the LED on GPIO 2
led = machine.Pin(2, machine.Pin.OUT)
led.value(0)

# Set up the beeper on GPIO 6
beep = machine.Pin(6, machine.Pin.OUT)
beep.value(0)

# Set up GPIO 15 as input (default pulled up, LOW when triggered)
trigger = machine.Pin(15, machine.Pin.IN)

#flag for radiation detection
radiation_detected = False

# Interrupt handler function
def handle_radiation(pin):
    global radiation_detected
    radiation_detected = True #set flag on detection

# Attach interrupt to GPIO15 (triggers on FALLING EDGE)
trigger.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_radiation)


# Keep the script running
while True:
    if radiation_detected:
        for _ in range(1):  # Blink LED 5 times
            led.value(1)
            beep.value(0)
            utime.sleep(1)
            led.value(0)
            beep.value(0)
            utime.sleep(1)
            led.value(1)
            utime.sleep(1)
            led.value(0)
            utime.sleep(1)
        #playRandom.play_random_sound()  # Call function to play a random sound
        #playRandom.play_specific_sound()
        #playRandom.list_sd_files()       
        radiation_detected = False    
    utime.sleep(1)  # Keep the script alive
