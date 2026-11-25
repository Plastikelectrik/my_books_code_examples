import struct
import sys
import zlib

MAGIC = b"KTL1"
KINDS = ["green", "black", "oolong", "herbal"]


def read_ktl(data):
    if len(data) < 12 or data[:4] != MAGIC:
        raise ValueError("not a KTL file")
    version, count = struct.unpack_from("<HH", data, 4)
    if version != 2:
        raise ValueError(f"unsupported version {version}")
    end = 8 + 16 * count
    if len(data) != end + 4:
        raise ValueError("bad length")
    stored = struct.unpack_from("<I", data, end)[0]
    if stored != zlib.crc32(data[:end]):
        raise ValueError("bad checksum")
    recipes = []
    for i in range(count):
        off = 8 + 16 * i
        fields = struct.unpack_from("<BBH", data, off)
        kind, temp, secs = fields
        name = data[off + 4:off + 16].rstrip(b"\0")
        recipes.append((kind, temp, secs, name.decode()))
    return recipes


def write_ktl(recipes):
    body = MAGIC + struct.pack("<HH", 2, len(recipes))
    for kind, temp, secs, name in recipes:
        raw = name.encode("ascii").ljust(12, b"\0")
        head = struct.pack("<BBH", kind, temp, secs)
        body += head + raw
    return body + struct.pack("<I", zlib.crc32(body))


def main():
    cmd, src = sys.argv[1], sys.argv[2]
    with open(src, "rb") as f:
        recipes = read_ktl(f.read())
    if cmd == "show":
        for kind, temp, secs, name in recipes:
            print(KINDS[kind], temp, secs, name)
    elif cmd == "roundtrip":
        with open(sys.argv[3], "wb") as f:
            f.write(write_ktl(recipes))


if __name__ == "__main__":
    main()
