# Store a small map and query cells
grid_text = [
    "##########",
    "#........#",
    "#..###...#",
    "#....#...#",
    "#....#.#.#",
    "#......#.#",
    "##########",
]
grid = [[1 if ch == "#" else 0 for ch in row]
        for row in grid_text]
rows, cols = len(grid), len(grid[0])
free = sum(row.count(0) for row in grid)
print(f"map size: {rows} x {cols} cells")
print(f"free cells: {free} of {rows * cols}")

def is_free(r, c):
    inside = 0 <= r < rows and 0 <= c < cols
    return inside and grid[r][c] == 0

print("cell (1,1) free?", is_free(1, 1))
print("cell (2,3) free?", is_free(2, 3))
