from machine import I2S, Pin

# Configure I2S for your DAC
i2s = I2S(
    0,  # I2S bus ID (use 0 or 1)
    sck=Pin(35),   # BCLK (Bit Clock)
    ws=Pin(36),    # LRCK (Word Select / Left-Right Clock)
    sd=Pin(37),    # DOUT (Data Out)
    mode=I2S.TX,   # Transmit mode
    bits=16,       # 16-bit audio
    format=I2S.STEREO,
    rate=44100,    # Standard audio rate (adjust as needed)
    ibuf=20000     # Buffer size
)

print("I2S initialized successfully!")