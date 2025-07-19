import machine #used for GPIO
import utime
#60000 kHz seems to create the most voltage
# Create PWM on GPIO 41
pwm = machine.PWM(machine.Pin(41))
pwm.freq(60000)  # Set PWM frequency to 100 kHz (5µs high, 5µs low)
pwm.duty_u16(32767)  # 50% duty cycle (range 0-65535, so 32767 is 50%)

# Keep PWM running indefinitely
while True:
    utime.sleep(1)  # Sleep to keep the program running

