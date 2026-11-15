#!/usr/bin/env python3
"""Log CPU temperature and power problems every minute."""
import logging, subprocess, time
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s %(message)s")
log = logging.getLogger("health")
TEMP = Path("/sys/class/thermal/thermal_zone0/temp")

def read_temp():
    return int(TEMP.read_text()) / 1000

def read_throttled():
    cmd = ["vcgencmd", "get_throttled"]
    out = subprocess.run(cmd, capture_output=True,
                         text=True).stdout
    return int(out.strip().split("=")[1], 16)

while True:
    t, th = read_temp(), read_throttled()
    if th & 0x1:
        log.warning("under-voltage: check the supply")
    if t > 75:
        log.warning("high temperature: %.1f °C", t)
    else:
        log.info("ok: %.1f °C, flags=0x%x", t, th)
    time.sleep(60)
