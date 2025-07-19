import radiationIN
import playRandom
import utime
import os
import blink
import _thread  # Allows running radiation detection in a separate thread

blink.blink(5)  # Blink 5 times
# Start radiation detection in a separate thread
_thread.start_new_thread(radiationIN.handle_radiation, ())


# Keep main script running
while True:
    utime.sleep(1)  # Prevent CPU overuse

