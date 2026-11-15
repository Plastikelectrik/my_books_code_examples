from gpiozero import Button
from signal import pause
import subprocess

def shutdown():
    print("Held for 3 seconds: shutting down")
    subprocess.run(["sudo", "shutdown", "-h", "now"])

power = Button(3, bounce_time=0.05, hold_time=3)
power.when_held = shutdown
pause()
