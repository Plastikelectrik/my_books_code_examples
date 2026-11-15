import os, shutil, time
from pathlib import Path

def mem_used_percent():
    info = {}
    text = Path("/proc/meminfo").read_text()
    for line in text.splitlines():
        key, value = line.split(":")
        info[key] = int(value.split()[0])          # kB
    used = info["MemTotal"] - info["MemAvailable"]
    return 100 * used / info["MemTotal"]

def disk_used_percent(path="/"):
    total, used, free = shutil.disk_usage(path)
    return 100 * used / total

def load_per_core():
    return os.getloadavg()[0] / os.cpu_count()

def cpu_temp():
    p = Path("/sys/class/thermal/thermal_zone0/temp")
    if not p.exists():
        return None
    return int(p.read_text()) / 1000

def bar(percent, width=20):
    filled = int(round(percent / 100 * width))
    return "#" * filled + "." * (width - filled)

def report():
    rows = [("Memory", mem_used_percent()),
            ("Disk /", disk_used_percent()),
            ("Load", min(100, 100 * load_per_core()))]
    for name, pct in rows:
        print(f"{name:7s} [{bar(pct)}] {pct:5.1f} %")
    t = cpu_temp()
    print("CPU temp:", f"{t:.1f} °C" if t else "n/a")

print(time.strftime("%H:%M:%S"), "system health")
report()
