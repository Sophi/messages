import machine
import os

def mount_sd():
    try:
        # Check if already mounted
        if "/sd" in os.listdir("/"):
            print("SD card already mounted.")
            return True
    except Exception:
        pass

    try:
        sd = machine.SDCard(slot=2, width=1, sck=12, miso=13, mosi=11, cs=10, freq=5000000)
        try:
            os.umount("/sd")  # Best effort unmount
        except OSError as e:
            if e.args[0] == 2:  # Not mounted
                print("SD card was not mounted.")
            elif e.args[0] == 16:  # Already busy
                print("SD card busy. Proceeding without unmount.")
        os.mount(sd, "/sd")
        print("SD card mounted successfully.")
        return True
    except Exception as e:
        print("Failed to initialize SD card:", repr(e))
        return False
