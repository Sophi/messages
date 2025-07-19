import os #file ops
import math
import struct
import machine #for gpio
import sdcard
import uos #for filesystem mounting 
import random #random number generation functions
import time #delays
import ustruct
from machine import I2S, Pin, SDCard

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
    #rate=11000,    # Standard audio rate (adjust as needed)
    rate=44100,
    ibuf=100000     # I2S internal buffer size,
    #controls how much audio data is preloaded into I2S before playback
)

# Connect SD card to SPI pins
'''spi = machine.SPI(1, baudrate=2500000, sck=machine.Pin(12), mosi=machine.Pin(11), miso=machine.Pin(13))
cs = machine.Pin(10, machine.Pin.OUT)'''
sd = machine.SDCard(slot=2, width=1, sck=12, miso=13, mosi=11, cs=10, freq=25000000)
#cd=None, wp=None, cmd=None, data=None, 

#os.mount(sd,"/sd")
try:
    os.umount("/sd")  # Unmount if already mounted

except OSError:
    print("SD card was not mounted.")
    
os.mount(sd,"/sd")    
# Initialize SD card
#sd = sdcard.SDCard(spi, cs)
#uos.mount(sd, "/sd")
#uos.umount("/sd") just in case I need to unmount later 
# end SD card setup

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

def play_specific_sound():
    #file_path = "/sd/output_11000_mono.wav"
    #file_path = "/sd/scuse_me2_mono.wav"
    file_path = "/sd/final_pump.wav"
    #file_path = "/sd/lewis_balls2.wav"
    #file_path = "/sd/space-animal-stereo.wav"
    #file_path = "/sd/gong-bell-stereo.wav" #22500, MONO
    #file_path = "/sd/output.wav"
    #if file_path not in os.listdir("/sd"):
    if "lewis_balls2.wav" not in os.listdir("/sd"):
        print("File not found:", file_path)
        return
    print("Playing:", file_path)
    
    buffer_size = 24576  # Reduce chunk size to prevent SD timeout
    #Controls how much data is read from the SD card at a time
    audio_buffer = bytearray(buffer_size)

    with open(file_path, "rb") as f:
        f.read(44)  # Skip WAV header

        while True:
            bytes_read = f.readinto(audio_buffer)  # Read into buffer
            #time.sleep(0.01)
            #print (audio_buffer)
            if not bytes_read:
                break       
            i2s.write(audio_buffer[:bytes_read])  # Write to I2S in small chunks
            # Convert 16-bit PCM to properly aligned I2S 16-bit format

    print("Playback finished")
    
def play_specific_soundA():
    #file_path = "/sd/final_pump.wav"
    file_path = "/sd/final_pump_clip.wav"
    #file_path = "/sd/lewis_balls2.wav"
    if "final_pump_clip.wav" not in os.listdir("/sd"):
        print("File not found:", file_path)
        return
    print("Playing:", file_path)

    _BUFFER_SIZE = 8192  # Define buffer size
    buffer = bytearray(_BUFFER_SIZE)  
    bmv = memoryview(buffer)  # Create a memoryview for efficient slicing

    with open(file_path, "rb", _BUFFER_SIZE) as infile:
        infile.read(44)  # Skip WAV header

        while True:
            bytes_read = infile.readinto(bmv)  # Read directly into memoryview
            if bytes_read == _BUFFER_SIZE:
                i2s.write(bmv)  # Write full buffer
            else:
                i2s.write(bmv[:bytes_read])  # Write only valid data
            if bytes_read < _BUFFER_SIZE:
                break

    print("Playback finished")    

    
# Function to play a random .wav file
def play_random_sound():
    wav_files = [f for f in os.listdir("/sd") if f.lower().endswith(".wav")]
    if not wav_files:
        print("No .wav files found!")
        return

    random_file = random.choice(wav_files)
    print("Playing:", random_file)

    with open("/sd/" + random_file, "rb") as f:
        f.read(44)  # Skip WAV header

        while True:
            audio_data = f.read(1024)  # Read in chunks
            if not audio_data:
                break
            i2s.write(audio_data)  # Send to DAC

    print("Playback finished")


# Example usage:
list_sd_files()
#play_random_sound()
play_specific_sound()