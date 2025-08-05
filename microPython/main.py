import utime
import os
import blink

import sdutils
utime.sleep(0.5)
sdutils.mount_sd()

import playRandom
import radiationIN
import _thread  # Allows running radiation detection in a separate thread

print("Starting main.py")
blink.blink(3)  # Blink 5 times

print("Blink finished")

# Start radiation detection in a separate thread
_thread.start_new_thread(radiationIN.handle_radiation, ())

# Keep main script running
while True:
    utime.sleep(1)  # Prevent CPU overuse



