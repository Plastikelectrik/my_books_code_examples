import numpy as np
import sounddevice as sd

RATE = 16000
FRAME = 1280  # 80 ms, as openWakeWord expects

def find_device(part, kind="input"):
    for i, d in enumerate(sd.query_devices()):
        channels = d[f"max_{kind}_channels"]
        if part.lower() in d["name"].lower() and channels:
            return i
    raise RuntimeError(f"no {kind} device: {part!r}")

def frames(device):
    """Yield 80 ms frames of int16 audio forever."""
    with sd.InputStream(samplerate=RATE, channels=1,
                        dtype="int16", blocksize=FRAME,
                        device=device) as stream:
        while True:
            data, _ = stream.read(FRAME)
            yield data[:, 0].copy()

def play(samples, rate, device=None):
    sd.play(samples, rate, device=device)
    sd.wait()
