#cosmicRay #v9 sept 18, 2025
import machine
import utime
import time
import _thread
import os
import random
import playRandom  # Import the sound playback module
import lamp

def random_pink():
    """Return a richer, medium-light pink/purple RGB color."""
    r = random.randint(0, 255)   # strong but not max red
    g = random.randint(0, 0)      # keep green low
    b = random.randint(0, 255)   # blue medium-high
    return (r, g, b)
#Generated color: (209, 60, 196)
#Generated color: (186, 32, 188)
#60000 kHz seems to create the most voltage
# Create PWM on GPIO 41
pwm = machine.PWM(machine.Pin(41))
pwm.freq(60000)  # Set PWM frequency to 100 kHz (5µs high, 5µs low)
pwm.duty_u16(32767)  # 50% duty cycle (range 0-65535, so 32767 is 50%)

# Set up the LED on GPIO 2
led = machine.Pin(2, machine.Pin.OUT)
led.value(0)


# Set up GPIO 15 as input (default pulled up, LOW when triggered)
trigger = machine.Pin(15, machine.Pin.IN)

#flag for radiation detection
radiation_detected = False
hit_counter = 0
threshold = 10
print("cosmicRay v9 RGB LED, random color") #v9 sept 18, 2025

# Interrupt handler function
def irq_handler(pin):
    global radiation_detected
    radiation_detected = True

trigger.irq(trigger=machine.Pin.IRQ_FALLING, handler=irq_handler)

def handle_radiation():
    global radiation_detected, hit_counter, threshold
    print("cosmic ray gathering started")

   # Timer variables
    interval_start = time.time()
    hits_in_interval = 0
    interval_seconds = 10  # measure hits every 5 seconds
    
    while True:
        if radiation_detected:          
            hit_counter += 1
            hits_in_interval += 1
            print("cosmic ray! hit#", hit_counter)
            radiation_detected = False
       
        if hit_counter >= threshold:
            print("cosmic ray threshold reached!", hit_counter)
            # Start both simultaneously in separate threads
            _thread.start_new_thread(lamp.pulse,(random_pink(),))

            utime.sleep(1)
            _thread.start_new_thread(playRandom.play_random_sound, ())
            
            # Wait for effects to finish (pulse takes ~5 seconds)
            utime.sleep(6)
        
            led.value(1)
            utime.sleep(1)
            led.value(0)
            utime.sleep(1)
            hit_counter = 0
            
             # Timer check
        now = time.time()
        if now - interval_start >= interval_seconds:
            #print(f"Hits in last {interval_seconds} sec: {hits_in_interval}")
            hits_in_interval = 0
            interval_start = now
            
        utime.sleep(0.05)  # avoid hogging CPU
