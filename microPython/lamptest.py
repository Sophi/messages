# MicroPython WS2812 simple test
import machine, neopixel, time

PIN_NUM = 48        # <--- set this to your data pin number
NUM_LEDS = 50       # <--- set to how many LEDs you have

pin = machine.Pin(PIN_NUM, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, NUM_LEDS)

def set_all(r,g,b):
    for i in range(NUM_LEDS):
        np[i] = (r,g,b)
    np.write()

# Test sequence
set_all(255,0,255)   # pink
time.sleep(1)
set_all(255,0,0)     # red
time.sleep(0.5)
set_all(0,255,0)     # green
time.sleep(0.5)
set_all(0,0,255)     # blue
time.sleep(0.5)
set_all(0,0,0)       # off
time.sleep(.5)
set_all(223, 0, 255)
time.sleep(1)
set_all(146, 0, 255)
time.sleep(1)
set_all(197, 0, 255)
time.sleep(1)
set_all(255, 0, 255)
time.sleep(1)
set_all(255, 0, 255)
time.sleep(1)
set_all(255, 0, 255)
time.sleep(2)
set_all(0, 0, 0)