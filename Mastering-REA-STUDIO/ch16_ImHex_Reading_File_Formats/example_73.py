import struct
import sys
import zlib

KINDS = {"green": 0, "black": 1, "oolong": 2, "herbal": 3}


def record(name, temp, secs):
    raw = name.encode("ascii")[:12].ljust(12, b"\0")
    head = struct.pack("<BBH", KINDS[name], temp, secs)
    return head + raw


def build(recipes):
    body = b"KTL1" + struct.pack("<HH", 2, len(recipes))
    for r in recipes:
        body += record(*r)
    return body + struct.pack("<I", zlib.crc32(body))


if __name__ == "__main__":
    recs = [("green", 80, 130), ("black", 95, 240),
            ("oolong", 90, 180)]
    with open(sys.argv[1], "wb") as f:
        f.write(build(recs))
