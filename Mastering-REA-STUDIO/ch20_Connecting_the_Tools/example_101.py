import csv
import itertools
import subprocess
import sys

target, out_csv = sys.argv[1:3]
teas = ["green", "black", "oolong", "herbal", "mint"]
strengths = ["1", "2", "3", "4", "5", "0", "9", "abc"]

with open(out_csv, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["tea", "strength", "exit", "stdout"])
    for tea, s in itertools.product(teas, strengths):
        p = subprocess.run([target, tea, s],
                           capture_output=True,
                           text=True, timeout=5)
        w.writerow([tea, s, p.returncode,
                    p.stdout.strip()])
