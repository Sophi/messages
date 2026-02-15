#main
import utime
import os
import blink
import lamp

import sdutils
utime.sleep(0.5)
sdutils.mount_sd()

import playRandom
import cosmicRay
#import cosmicRay2
import _thread  # Allows running radiation udetection in a separate thread	`

lamp.clear()
print("Starting main.py")
blink.blink(1)  # Blink 5 times

print("Blink finished")

# Start radiation detection in a separate thread
_thread.start_new_thread(cosmicRay.handle_radiation, ())

# Keep main script running
while True:
    utime.sleep(1)  # Prevent CPU overuse



