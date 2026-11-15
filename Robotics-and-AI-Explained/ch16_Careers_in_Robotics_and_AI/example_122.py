# Find the most requested skills in job texts
from collections import Counter
import re

ads = [
    "Robot software engineer: Python, C++, ROS 2, Linux,"
    " computer vision. Experience with Git and testing.",
    "Automation technician: PLC, electronics, sensors,"
    " robot maintenance, safety, teamwork.",
    "Machine learning engineer: Python, PyTorch, data,"
    " computer vision, Linux, communication skills.",
    "Integration engineer: ROS 2, Python, safety,"
    " sensors, customer communication, travel.",
]
skills = ["python", "c++", "ros 2", "linux",
          "computer vision", "git", "plc", "electronics",
          "sensors", "safety", "pytorch", "data",
          "communication", "teamwork"]
count = Counter()
for ad in ads:
    text = ad.lower()
    for s in skills:
        if re.search(re.escape(s), text):
            count[s] += 1
for skill, n in count.most_common(6):
    print(f"{skill:16s} in {n} of {len(ads)} ads")
