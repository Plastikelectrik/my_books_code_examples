import time
from kodi_rpc import call, DRY_RUN    # the client above

def sleep_timer(minutes, start_volume=60, steps=6):
    wait = minutes * 60 / steps
    for i in range(steps, -1, -1):
        call("Application.SetVolume",
             volume=start_volume * i // steps)
        if i and not DRY_RUN:
            time.sleep(wait)
    call("Player.Stop", playerid=1)

sleep_timer(30, steps=3)
