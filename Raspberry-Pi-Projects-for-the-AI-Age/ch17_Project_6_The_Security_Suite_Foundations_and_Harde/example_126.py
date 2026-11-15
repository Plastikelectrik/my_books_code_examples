import re
from collections import Counter, defaultdict

LOG = [
    "Failed password for root from 203.0.113.9",
    "Failed password for root from 203.0.113.9",
    "Failed password for invalid user admin "
    "from 203.0.113.9",
    "Invalid user test from 198.51.100.4",
    "Accepted publickey for oscar from 192.168.1.20",
    "Failed password for root from 203.0.113.9",
    "Failed password for root from 203.0.113.9",
]
FAILED = re.compile(
    r"(?:Failed password for (?:invalid user )?"
    r"(?P<u1>\S+)|Invalid user (?P<u2>\S+))"
    r" from (?P<ip>[\d.]+)")
OK = re.compile(r"Accepted (\S+) for (\S+) from ([\d.]+)")

def analyze(lines):
    fails, users, logins = Counter(), defaultdict(set), []
    for line in lines:
        if m := FAILED.search(line):
            fails[m["ip"]] += 1
            users[m["ip"]].add(m["u1"] or m["u2"])
        elif m := OK.search(line):
            logins.append(m.groups())
    return fails, users, logins

fails, users, logins = analyze(LOG)
for ip, n in fails.most_common():
    flag = "BLOCK" if n >= 5 else "watch"
    names = ", ".join(sorted(users[ip]))
    print(f"{flag:5s} {ip:13s} {n} fails ({names})")
for method, user, ip in logins:
    print(f"OK    {user} via {method} from {ip}")
