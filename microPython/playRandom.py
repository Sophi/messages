#playRandom v2
import os #file ops
import math
import random
import struct
import machine #for gpio
import sdcard
import uos #for filesystem mounting 
import time #delays
import utime
import ustruct
from machine import I2S, Pin, SDCard

sound_files = [f for f in os.listdir("/sd") if f.lower().endswith(".wav")]
unplayed_files = sound_files.copy()

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
    format=I2S.STEREO,
    #format=I2S.MONO,
    rate=44100, #rate=11000,    # Standard audio rate (adjust as needed)
    ibuf=100000     # I2S internal buffer size,
    #controls how much audio data is preloaded into I2S before playback
)

# initialize DAC
DAC = machine.Pin(14, machine.Pin.OUT)
DAC.value(1)

def list_sd_files():
    try:
        files = os.listdir("/sd")  # List all files in the SD card root
        print(" ")
        print("Files on SD card:")
        for file in files:
            print(file)
    except Exception as e:
        print("Error accessing SD card:", e)

# Function to play a random .wav file
def play_random_sound():
    print ("PlayRandom v2") #v2
    global unplayed_files

    if not sound_files:
        print("No .wav files found!")
        return

    if not unplayed_files:
        # All files have been played — reset the pool
        unplayed_files = sound_files.copy()

    # Pick a random file from the unplayed pool
    chosen_file = random.choice(unplayed_files)
    unplayed_files.remove(chosen_file)  # remove so it won't repeat
    print("Playing:", chosen_file)

    # Playback logic (your existing code)
    with open("/sd/" + chosen_file, "rb") as f:
        f.read(44)  # Skip WAV header
        utime.sleep_us(10)
        while True:
            audio_data = f.read(8192)  # Read in chunks
            if not audio_data:
                break
            i2s.write(audio_data)  # Send to DAC

    print("Playback finished")
    
