def follow_ball(x, radius, width=320,
                target_radius=45):
    """Return (left, right) speeds from -255 to 255."""
    err_x = (x - width / 2) / (width / 2)  # -1..+1
    turn = 120 * err_x                     # P control
    # drive forward until the ball looks big enough
    if radius < target_radius:
        base = 140
    else:
        base = 0
    left = max(-255, min(255, base + turn))
    right = max(-255, min(255, base - turn))
    return int(left), int(right)

for x, r in [(160, 20), (60, 20), (300, 20), (165, 50)]:
    cmd = follow_ball(x, r)
    print(f"ball x={x:3d} r={r}: motors {cmd}")
