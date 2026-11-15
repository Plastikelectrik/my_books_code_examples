import os, time, tempfile

def speed_test(folder, size_mb=64):
    data = os.urandom(1024 * 1024)
    path = os.path.join(folder, "speedtest.bin")
    t0 = time.perf_counter()
    with open(path, "wb") as f:
        for _ in range(size_mb):
            f.write(data)
        f.flush()
        os.fsync(f.fileno())
    write = size_mb / (time.perf_counter() - t0)
    t0 = time.perf_counter()
    with open(path, "rb") as f:
        while f.read(1024 * 1024):
            pass
    read = size_mb / (time.perf_counter() - t0)
    os.remove(path)
    return write, read

w, r = speed_test(tempfile.gettempdir(), 32)
print(f"write: {w:7.0f} MB/s")
print(f"read : {r:7.0f} MB/s (may come from the cache)")
