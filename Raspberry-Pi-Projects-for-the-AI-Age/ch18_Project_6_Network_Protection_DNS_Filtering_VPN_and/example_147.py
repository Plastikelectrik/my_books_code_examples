import re

NEIGH = """\
192.168.1.1 dev eth0 lladdr a4:91:b1:00:00:01 REACHABLE
192.168.1.20 dev eth0 lladdr 3c:22:fb:00:00:20 STALE
192.168.1.35 dev eth0 lladdr 02:5f:9a:12:34:56 REACHABLE
192.168.1.40 dev eth0 lladdr d8:3a:dd:00:00:40 DELAY
192.168.1.77 dev eth0  FAILED"""
KNOWN = {"a4:91:b1:00:00:01": "router",
         "3c:22:fb:00:00:20": "laptop",
         "d8:3a:dd:00:00:40": "media center"}
LINE = re.compile(r"^(\S+) dev \S+ lladdr (\S+) (\S+)")

def devices(text):
    for line in text.splitlines():
        if m := LINE.match(line):
            yield m.groups()

def is_random_mac(mac):
    return int(mac.split(":")[0], 16) & 0b10 != 0

new = []
for ip, mac, state in devices(NEIGH):
    name = KNOWN.get(mac.lower())
    if not name:
        new.append(ip)
        name = ("NEW, random MAC (phone?)"
                if is_random_mac(mac) else "NEW device!")
    print(f"{ip:13s} {mac} {name}")
print("alert for:", new)
