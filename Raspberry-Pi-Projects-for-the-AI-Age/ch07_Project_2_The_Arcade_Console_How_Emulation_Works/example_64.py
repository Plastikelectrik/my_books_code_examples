FRAME_MS = 1000 / 60          # one frame at 60 Hz

EMU = 2 * FRAME_MS           # emulator: about two frames
setups = {   # controller, emulator, display (ms)
    "Bartop, USB encoder, monitor": [1, EMU, 10],
    "TV, USB pad, game mode":       [4, EMU, 20],
    "TV, Bluetooth pad, normal mode": [12, EMU, 80],
}
for name, (pad, emulator, display) in setups.items():
    total = pad + emulator + display
    frames = total / FRAME_MS
    print(f"{name}")
    print(f"   {total:5.1f} ms = {frames:.1f} frames")
