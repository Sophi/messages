import math
import struct
from machine import I2S
from machine import Pin

# setup
# Configure I2S for your DAC
i2s = I2S(
    0,  # I2S bus ID (use 0 or 1)
    sck=Pin(35),   # BCLK (Bit Clock)
    ws=Pin(36),    # LRCK (Word Select / Left-Right Clock)
    sd=Pin(37),    # DOUT (Data Out)
    mode=I2S.TX,   # Transmit mode
    bits=16,       # 16-bit audio
    #bits=32,       # 32-bit audio
    #format=I2S.STEREO,
    format=I2S.MONO,
    #rate=44100,    # Standard audio rate (adjust as needed)
    rate=44100,
    ibuf=2000     # Buffer size
)

def make_tone(rate, bits, frequency):
    samples_per_cycle = rate // frequency
    sample_size_in_bytes = bits // 8
    samples = bytearray(samples_per_cycle * sample_size_in_bytes)
    volume = pow(2, bits) // 4

    for i in range(samples_per_cycle):
        sample = int(volume * math.sin(2 * math.pi * i / samples_per_cycle))
        struct.pack_into("<h", samples, i * sample_size_in_bytes, sample)
    
    return samples

samples = make_tone(22050, 16, 440)

while True:
    i2s.write(samples)