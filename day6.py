from aoc import get_input, submit
from utils import Vector2D

#TODO: super slow

def in_bounds(grid, pos):
    return 0 <= pos.y < len(grid) and 0 <= pos.x < len(grid[pos.y])

def find_start(grid):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '^':
                return Vector2D(x, y), Vector2D(0, -1)

def patrol(grid):
    pos, dir = find_start(grid)
    path = set()
    path.add(pos)
    while True:
        new_pos = pos + dir
        if not in_bounds(grid, new_pos):
            return path
        if grid[new_pos.y][new_pos.x] == '#':
            dir = dir.rot90()
        else:
            pos = new_pos
            path.add(pos)

def loops(grid, obstacle):
    pos, dir = find_start(grid)
    seen = set()
    while True:
        if (pos, dir) in seen:
            return True
        seen.add((pos, dir))
        new_pos = pos + dir
        if not in_bounds(grid, new_pos):
            return False
        if grid[new_pos.y][new_pos.x] == '#' or new_pos == obstacle:
            dir = dir.rot90()
        else:
            pos = new_pos

grid = get_input(6).splitlines()
path = patrol(grid)
submit(len(path))
submit(sum(loops(grid, pos) for pos in path if grid[pos.y][pos.x] == '.'))
