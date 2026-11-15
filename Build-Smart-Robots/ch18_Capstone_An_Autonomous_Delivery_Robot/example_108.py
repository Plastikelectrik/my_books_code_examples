"""Capstone: an autonomous delivery robot (simulation)."""
import heapq
import math
import numpy as np

RES = 0.05                         # m per cell
ROWS, COLS = 60, 80                # 3 m x 4 m room

# ---------- world ----------
def make_room():
    g = np.zeros((ROWS, COLS), np.uint8)
    g[0, :] = g[-1, :] = g[:, 0] = g[:, -1] = 1
    g[0:40, 20:24] = 1             # wall from bottom
    g[25:60, 50:54] = 1            # wall from top
    return g

def inflate(g, r_cells=3):
    out = g.copy()
    for r, c in zip(*np.nonzero(g)):
        out[max(0, r - r_cells):r + r_cells + 1,
            max(0, c - r_cells):c + r_cells + 1] = 1
    return out

def cell(x, y):
    return int(y / RES), int(x / RES)

def meters(rc):
    return (rc[1] + 0.5) * RES, (rc[0] + 0.5) * RES

# ---------- planning ----------
def astar(g, s, goal):
    moves = [(1, 0, 1), (-1, 0, 1), (0, 1, 1),
             (0, -1, 1), (1, 1, 1.41), (1, -1, 1.41),
             (-1, 1, 1.41), (-1, -1, 1.41)]
    h = lambda n: math.dist(n, goal)
    heap, came, cost = [(h(s), 0, s)], {s: None}, {s: 0}
    while heap:
        _, c, cur = heapq.heappop(heap)
        if cur == goal:
            path = []
            while cur:
                path.append(cur)
                cur = came[cur]
            return path[::-1]
        if c > cost[cur]:
            continue
        for dr, dc, st in moves:
            n = (cur[0] + dr, cur[1] + dc)
            if not (0 <= n[0] < ROWS
                    and 0 <= n[1] < COLS):
                continue
            if g[n] or c + st >= cost.get(n, 1e9):
                continue
            cost[n], came[n] = c + st, cur
            heapq.heappush(heap,
                           (c + st + h(n), c + st, n))
    return None

def plan(g, start_xy, goal_xy):
    g = g.copy()
    r, c = cell(*start_xy)          # the robot's own
    g[r - 1:r + 2, c - 1:c + 2] = 0  # cell is free
    p = astar(g, (r, c), cell(*goal_xy))
    if p is None:
        return None
    return [meters(rc) for rc in p[::4]] + [goal_xy]

# ---------- control ----------
def pure_pursuit(pose, path, look=0.25, v=0.2):
    x, y, th = pose
    target = path[-1]
    for p in path:
        if math.dist(p, (x, y)) >= look:
            target = p
            break
    a = math.atan2(target[1] - y, target[0] - x) - th
    a = math.atan2(math.sin(a), math.cos(a))
    speed = v * max(0.2, math.cos(a))
    return speed, 2 * speed * math.sin(a) / look

def prune(path, pose):
    """Drop waypoints we have already passed."""
    while len(path) > 1 and \
            math.dist(path[0], pose[:2]) < 0.15:
        path.pop(0)

# ---------- mission (state machine) ----------
STATIONS = {"home": (0.4, 0.4), "kitchen": (1.6, 2.6),
            "office": (3.6, 0.4)}

def run_mission(stops, block_at=None, dt=0.1):
    room = make_room()             # the real world
    seen = room.copy()             # what the robot knows
    known = inflate(seen)
    pose = [*STATIONS["home"], 0.0]
    battery, t, log = 100.0, 0.0, []
    queue = list(stops) + ["home"]
    state, path, goal, wait = "PLAN", None, None, 0
    replans, blocked = 0, False
    while queue or state != "DONE":
        if state == "PLAN":
            if not queue:
                state = "DONE"
                break
            goal = queue.pop(0)
            path = plan(known, pose[:2], STATIONS[goal])
            if path is None:
                log.append(f"{t:5.1f}s no path to {goal}")
                state = "DONE"
                break
            log.append(f"{t:5.1f}s heading to {goal}, "
                       f"{len(path)} waypoints")
            state = "DRIVE"
        elif state == "DRIVE":
            # an unexpected box appears once on the route
            if block_at and not blocked and t >= block_at:
                bx, by = path[min(4, len(path) - 1)]
                r, c = cell(bx, by)
                room[r - 2:r + 3, c - 2:c + 3] = 1
                blocked = True
            # "sensor": look 0.3 m ahead in the real room
            ax = pose[0] + 0.3 * math.cos(pose[2])
            ay = pose[1] + 0.3 * math.sin(pose[2])
            ahead = cell(ax, ay)
            if room[ahead] and not seen[ahead]:
                seen = room.copy()     # map the new box
                known = inflate(seen)
                path = plan(known, pose[:2],
                            STATIONS[goal])
                replans += 1
                log.append(f"{t:5.1f}s obstacle: replan")
                if path is None:
                    log.append(f"{t:5.1f}s blocked, stop")
                    state = "DONE"
                    break
            prune(path, pose)
            if math.dist(pose[:2], STATIONS[goal]) < 0.08:
                log.append(f"{t:5.1f}s arrived at {goal}")
                state, wait = "WAIT", 20
                continue
            v, w = pure_pursuit(pose, path)
            pose[0] += v * math.cos(pose[2]) * dt
            pose[1] += v * math.sin(pose[2]) * dt
            pose[2] += w * dt
            battery -= 0.02 + 0.1 * v * dt
        elif state == "WAIT":       # unload / load
            wait -= 1
            if wait == 0:
                state = "PLAN"
        t += dt
        if battery < 20 or t > 600:
            log.append(f"{t:5.1f}s abort: battery/time")
            break
    return log, battery, t, replans

if __name__ == "__main__":
    log, batt, t, rp = run_mission(
        ["kitchen", "office"], block_at=22.0)
    print("\n".join(log))
    print(f"mission time {t:.0f} s, battery {batt:.0f} %,"
          f" replans {rp}")
