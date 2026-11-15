from pathlib import Path

def cpu_temp_c():
    raw = Path("/sys/class/thermal/thermal_zone0/temp")
    return int(raw.read_text()) / 1000

print(f"CPU temperature: {cpu_temp_c():.1f} °C")
