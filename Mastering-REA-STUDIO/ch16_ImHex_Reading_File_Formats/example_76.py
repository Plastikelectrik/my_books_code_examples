import struct
import sys
import zlib

data = open(sys.argv[1], "rb").read()
body, tail = data[:-4], data[-4:]
stored = struct.unpack("<I", tail)[0]
computed = zlib.crc32(body)
print(f"stored={stored:#010x} computed={computed:#010x}")
sys.exit(0 if stored == computed else 1)
