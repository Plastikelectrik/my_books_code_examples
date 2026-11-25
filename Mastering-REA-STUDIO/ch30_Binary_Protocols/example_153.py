import socket
import sys


def pairs(path):
    req = None
    for line in open(path):
        side, data = line.split()
        if side == "C":
            req = bytes.fromhex(data)
        elif req is not None:
            yield req, bytes.fromhex(data)
            req = None


host, port = sys.argv[2], int(sys.argv[3])
diffs = total = 0
with socket.create_connection((host, port)) as s:
    for req, expected in pairs(sys.argv[1]):
        s.sendall(req)
        got = s.recv(4096)
        total += 1
        if got != expected:
            diffs += 1
            print("DIFF", req.hex(), expected.hex(),
                  got.hex())
print(f"{total} exchanges, {diffs} differences")
sys.exit(1 if diffs else 0)
