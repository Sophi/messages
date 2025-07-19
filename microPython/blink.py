from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

def blink(times=5, pin=2, delay=0.5):
    led = Pin(pin, Pin.OUT)
    for _ in range(times):
        led.value(1)
        sleep(delay)
        led.value(0)
        sleep(delay)

#while True:
    #led.value(1)
    #sleep(0.5)
    #led.value(0)
    #sleep(0.5)
