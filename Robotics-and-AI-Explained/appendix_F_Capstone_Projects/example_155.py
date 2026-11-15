import heapq

GRID = ["..........",
        ".##.##.##.",
        ".##.##.##.",
        "..........",
        ".##.##.##.",
        "..........",]
DOCK, PACK = (5, 0), (0, 9)
SHELVES = {"A": (0, 3), "B": (3, 6), "C": (5, 9)}

def astar(start, goal):
    open_set = [(0, 0, start, None)]
    came, cost = {}, {start: 0}
    while open_set:
        _, g, cell, parent = heapq.heappop(open_set)
        if cell in came:
            continue
        came[cell] = parent
        if cell == goal:
            break
        r, c = cell
        for nr, nc in [(r+1, c), (r-1, c),
                       (r, c+1), (r, c-1)]:
            if 0 <= nr < 6 and 0 <= nc < 10 \
                    and GRID[nr][nc] == "." \
                    and g + 1 < cost.get((nr, nc), 99):
                cost[(nr, nc)] = g + 1
                h = abs(nr - goal[0]) + abs(nc - goal[1])
                item = (g + 1 + h, g + 1, (nr, nc), cell)
                heapq.heappush(open_set, item)
    path, cell = [], goal
    while cell is not None:
        path.append(cell)
        cell = came[cell]
    return path[::-1]

battery, pos, state = 100.0, DOCK, "IDLE"
orders = ["A", "C", "B", "A"]
PCT_PER_CELL, RESERVE = 1.0, 30.0   # battery %
while orders or state != "IDLE":
    if state == "IDLE":
        shelf = SHELVES[orders[0]]
        cells = (len(astar(pos, shelf))
                 + len(astar(shelf, PACK))
                 + len(astar(PACK, DOCK)) - 3)
        trip = cells * PCT_PER_CELL
        if battery - trip < RESERVE:
            print(f"battery {battery:.0f}%, trip needs "
                  f"{trip:.0f}% -> CHARGING")
            battery, state = 100.0, "IDLE"
            continue
        order = orders.pop(0)
        state, goal = "TO_SHELF", shelf
    elif state == "TO_SHELF":
        state, goal = "TO_PACK", PACK
    elif state == "TO_PACK":
        state, goal = "RETURN", DOCK
    elif state == "RETURN":
        print(f"order {order} done, "
              f"battery {battery:.0f}%")
        state = "IDLE"
        continue
    path = astar(pos, goal)
    battery -= (len(path) - 1) * PCT_PER_CELL
    pos = goal
print("all orders delivered")
