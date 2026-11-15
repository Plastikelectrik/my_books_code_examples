import numpy as np

def record_command(frame_iter, silence_s=0.8, max_s=8.0,
                   rate=16000, frame=1280):
    """Return float32 audio of one spoken command."""
    noise = None
    chunks, quiet, heard = [], 0.0, False
    step = frame / rate
    for i, f in enumerate(frame_iter):
        x = f.astype(np.float32) / 32768
        rms = float(np.sqrt((x ** 2).mean()))
        if noise is None:
            noise = max(rms, 1e-4)       # first frame
        chunks.append(x)
        if rms > noise * 3:
            heard, quiet = True, 0.0
        elif heard:
            quiet += step
        if heard and quiet >= silence_s:
            break
        if (i + 1) * step >= max_s:
            break
    return np.concatenate(chunks)
