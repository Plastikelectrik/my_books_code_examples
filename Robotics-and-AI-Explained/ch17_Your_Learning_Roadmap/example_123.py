# Pick projects that match your skills and time
projects = [
    ("sensor logger", 1, 5),
    ("obstacle robot", 2, 15),
    ("line follower PID", 3, 20),
    ("color tracker", 3, 25),
    ("voice control", 3, 20),
    ("mapping robot", 4, 40),
    ("ROS 2 simulation", 4, 40),
    ("learning arm", 5, 60),
]   # (name, difficulty 1-5, hours)

my_level = 3
hours_available = 25
options = [p for p in projects
           if my_level - 1 <= p[1] <= my_level + 1
           and p[2] <= hours_available]
for name, diff, hours in options:
    print(f"{name:18s} difficulty {diff}, ~{hours} h")
