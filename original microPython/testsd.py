import machine
import os
import utime

# Make sure mount point exists
try:
    os.stat("/sd")
except OSError:
    os.mkdir("/sd")

print("Initializing SD card...")

try:
    sd = machine.SDCard(slot=2, width=1, sck=12, miso=13, mosi=11, cs=10, freq=25000000)
    os.mount(sd, "/sd")
    print("SD card mounted successfully!")
except Exception as e:
    print("Failed to mount SD card:", e)
    while True:
        utime.sleep(1)  # Halt here

print("Listing files on SD card:")
try:
    files = os.listdir("/sd")
    for f in files:
        print(f)
except Exception as e:
    print("Failed to list files:", e)

while True:
    utime.sleep(1)  # Keep running
