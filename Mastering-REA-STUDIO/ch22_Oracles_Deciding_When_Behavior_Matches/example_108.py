import itertools
import shlex
import subprocess
import sys

TEAS = ["green", "black", "oolong", "herbal", "mint",
        "", "GREEN", "green "]
STRENGTHS = [None, "1", "3", "5", "0", "6", "-1",
             "abc", "4x", " 4", "+4", "04"]


def run(cmd, args):
    p = subprocess.run(cmd + args, capture_output=True,
                       text=True, timeout=5)
    return p.returncode, p.stdout


def main():
    original = shlex.split(sys.argv[1])
    rebuild = shlex.split(sys.argv[2])
    cases = [[]]
    for tea, s in itertools.product(TEAS, STRENGTHS):
        cases.append([tea] if s is None else [tea, s])
    failures = 0
    for args in cases:
        a, b = run(original, args), run(rebuild, args)
        if a != b:
            failures += 1
            print("DIFF", args, a, b)
    print(f"{len(cases)} cases, {failures} differences")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
