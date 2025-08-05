import machine
import utime

# Set up the LED on GPIO 2
led = machine.Pin(2, machine.Pin.OUT)

# Blink LED on GPIO 2 5 times
def blink(times=5, pin=2):
    led = machine.Pin(pin, machine.Pin.OUT)
    for _ in range(times):
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        utime.sleep(0.5)
