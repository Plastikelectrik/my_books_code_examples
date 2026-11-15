# Plan review dates for each topic you learn
from datetime import date, timedelta

intervals = [1, 3, 7, 21]          # days after learning
topics = {"PID control": date(2026, 3, 2),
          "A* search": date(2026, 3, 4),
          "Kalman filter": date(2026, 3, 9)}

for topic, learned in topics.items():
    reviews = [learned + timedelta(days=d)
               for d in intervals]
    days = ", ".join(r.strftime("%d %b") for r in reviews)
    print(f"{topic:13s}: {days}")
