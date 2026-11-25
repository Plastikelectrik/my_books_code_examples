import hashlib
import sys
from pathlib import Path

root = Path(sys.argv[1])
print("| File | Bytes | SHA-256 (first 16) |")
print("| --- | --- | --- |")
for p in sorted(root.rglob("*")):
    if not p.is_file():
        continue
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    rel = p.relative_to(root)
    size = p.stat().st_size
    print(f"| {rel} | {size} | {h[:16]} |")
