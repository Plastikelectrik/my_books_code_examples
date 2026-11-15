from statistics import median

DRY_RAW, WET_RAW = 21000, 9500     # from calibration
THRESHOLD = 30                     # percent

def moisture_percent(raw):
    pct = (DRY_RAW - raw) / (DRY_RAW - WET_RAW) * 100
    return max(0.0, min(100.0, pct))

reminded = False
days = [[11000, 11200, 10900], [15800, 16100, 15950],
        [18200, 18400, 30000], [18600, 18500, 18700],
        [10200, 10100, 10300]]  # watered on the last day
for day, readings in enumerate(days, 1):
    pct = moisture_percent(median(readings))
    if pct < THRESHOLD and not reminded:
        note, reminded = "-> send reminder", True
    elif pct >= THRESHOLD:
        note, reminded = "", False
    else:
        note = "(already reminded)"
    print(f"day {day}: {pct:5.1f} % {note}")
