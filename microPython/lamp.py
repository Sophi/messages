#lamp v3
from machine import Pin
import neopixel
import utime
import _thread  


# NeoPixel setup
n = 75
lamp = Pin(48, Pin.OUT)  # GPIO connected to DIN
np = neopixel.NeoPixel(lamp, n, bpp=3)  # RGBW strip

def pulse(color, fade_in_time=1.0, fade_out_time=0.3, step_delay=0.02):
    """
    Alternative approach: specify total fade times instead of steps.
    - color: (R, G, B)
    - fade_in_time: total time for fade in (seconds)
    - fade_out_time: total time for fade out (seconds) 
    - step_delay: delay between each step
    """
    fade_in_steps = int(fade_in_time / step_delay)
    fade_out_steps = int(fade_out_time / step_delay)
    
    # Fade in
    for i in range(fade_in_steps):
        scale = i / fade_in_steps
        scaled_color = tuple(int(c * scale) for c in color)
        for j in range(n):
            np[j] = scaled_color
        np.write()
        utime.sleep(step_delay)
    
    # Fade out
    for i in range(fade_out_steps, -1, -1):
        scale = i / fade_out_steps
        scaled_color = tuple(int(c * scale) for c in color)
        for j in range(n):
            np[j] = scaled_color
        np.write()
        utime.sleep(step_delay)
    
    clear()

def clear():
    """Turn off all LEDs."""
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()