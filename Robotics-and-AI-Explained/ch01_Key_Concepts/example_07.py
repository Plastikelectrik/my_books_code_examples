# A cat-like agent moves toward the warmest room
temps = [12, 14, 17, 22, 19, 15]   # one value per room
position = 0

for step in range(8):
    here = temps[position]
    left = temps[position - 1] if position > 0 else -99
    right = (temps[position + 1]
             if position < len(temps) - 1 else -99)
    if right > here and right >= left:
        position += 1
    elif left > here:
        position -= 1
    else:
        print(f"step {step}: stays in room {position}"
              f" ({here} C)")
        break
    print(f"step {step}: moves to room {position}")
