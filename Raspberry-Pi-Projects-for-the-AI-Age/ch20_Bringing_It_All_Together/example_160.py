from datetime import date, timedelta

TASKS = {"check dashboard": 7, "full updates": 30,
         "restore test file": 30, "clean fans": 90,
         "run Lynis": 90, "image restore test": 365}
last_done = {"check dashboard": date(2026, 11, 2),
             "full updates": date(2026, 10, 1),
             "restore test file": date(2026, 10, 20),
             "clean fans": date(2026, 6, 1),
             "run Lynis": date(2026, 9, 1),
             "image restore test": date(2026, 1, 15)}

def due(today):
    for task, days in TASKS.items():
        next_date = last_done[task] + timedelta(days=days)
        if next_date <= today:
            late = (today - next_date).days
            yield task, late

today = date(2026, 11, 13)
for task, late in sorted(due(today), key=lambda x: -x[1]):
    print(f"DUE  {task:20s} ({late} days late)")
