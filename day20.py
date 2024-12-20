from aoc import get_input, submit
from utils import Vector2D

def find_path(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'S':
                start = Vector2D(x, y)
            elif c == 'E':
                end = Vector2D(x, y)
    path = []
    pos = start
    while pos != end:
        prev = path[-1] if path else None
        path.append(pos)
        pos = next(n for n in pos.neighbours() if grid[n.y][n.x] != '#' and n != prev)
    path.append(end)
    return path

def find_cheats_slow(grid, max_cheat_time):
    path = find_path(grid)
    for t1 in range(len(path)):
        for t2 in range(t1 + 1, len(path)):
            normal_time = t2 - t1
            cheat_time = abs(path[t2] - path[t1])
            if cheat_time <= max_cheat_time and cheat_time < normal_time:
                yield path[t1], path[t2], normal_time - cheat_time

def find_cheats_still_slow(grid, max_cheat_time):
    path = find_path(grid)

    normal_times = {}
    for time, pos in enumerate(path):
        normal_times[pos] = time

    for start in path:
        for cheat_time in range(2, max_cheat_time + 1):
            for end in boundary(start, cheat_time):
                if end in normal_times:
                    normal_time = normal_times[end] - normal_times[start]
                    if cheat_time < normal_time:
                        yield start, end, normal_time - cheat_time

def boundary(origin, radius):
    for i in range(1, radius + 1):
        yield Vector2D(origin.x + i, origin.y - radius + i)
        yield Vector2D(origin.x + radius - i, origin.y + i)
        yield Vector2D(origin.x - i, origin.y + radius - i)
        yield Vector2D(origin.x - radius + i, origin.y - i)

grid = get_input(20).splitlines()
submit(sum(saving >= 100 for _, _, saving in find_cheats_still_slow(grid, 2)))
submit(sum(saving >= 100 for _, _, saving in find_cheats_still_slow(grid, 20)))
