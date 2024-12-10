from aoc import get_input, submit
from functools import cache

input = get_input(10)
grid = [list(map(int, line)) for line in input.splitlines()]

@cache
def trail_ends(x, y):
    if grid[y][x] == 9:
        return { (x,y) }
    ends = set()
    for nx, ny in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] == grid[y][x] + 1:
            ends.update(trail_ends(nx, ny))
    return ends

@cache
def trail_rank(x, y):
    if grid[y][x] == 9:
        return 1
    rank = 0
    for nx, ny in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] == grid[y][x] + 1:
            rank += trail_rank(nx, ny)
    return rank

total_score = 0
total_rank = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == 0:
            total_score += len(trail_ends(x, y))
            total_rank += trail_rank(x, y)
submit(total_score)
submit(total_rank)
