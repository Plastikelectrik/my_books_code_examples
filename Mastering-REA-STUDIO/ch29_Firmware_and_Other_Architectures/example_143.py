import struct
import sys
import zlib

fs = open(sys.argv[1], "rb").read()
offset = 0x100
header = struct.pack("<4sHHII", b"KTFW", 1, 0,
                     offset, len(fs))
header += struct.pack("<I", zlib.crc32(fs))
image = header.ljust(offset, b"\xff") + fs
size = 1 << (len(image) - 1).bit_length()
image = image.ljust(size, b"\xff")
open(sys.argv[2], "wb").write(image)
print(f"image {len(image)} bytes, fs at {offset:#x}")
