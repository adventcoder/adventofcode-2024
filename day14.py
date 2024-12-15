from aoc import get_input, submit
from utils import Vector2D
from dataclasses import dataclass
from math import prod
from itertools import count

@dataclass
class Bot:
    pos: Vector2D
    vel: Vector2D

def parse_bot(s):
    kwargs = {}
    for token in s.split():
        l, r = token.split('=')
        if l == 'p':
            kwargs['pos'] = Vector2D.parse(r)
        elif l == 'v':
            kwargs['vel'] = Vector2D.parse(r)
    return Bot(**kwargs)

def quadrant(pos, size):
    middle = size // 2
    if pos.x == middle.x or pos.y == middle.y:
        return None
    x = int(pos.x > middle.x)
    y = int(pos.y > middle.y)
    return x + 2*y

def safety_factor(bots, t, size):
    counts = [0] * 4
    for bot in bots:
        pos = (bot.pos + bot.vel * t) % size
        i = quadrant(pos, size)
        if i is not None:
            counts[i] += 1
    return prod(counts)

def space(bots, t, size):
    grid = [['.'] * size.x for _ in range(size.y)]
    for bot in bots:
        pos = (bot.pos + bot.vel * t) % size
        grid[pos.y][pos.x] = '#'
    return grid

def easter_egg(grid):
    # look for 31 adjacent bots since that's the width of the picture
    for row in grid:
        if '#' * 31 in ''.join(row):
            return True
    return False

size = Vector2D(101, 103)
bots = [parse_bot(line) for line in get_input(14).splitlines()]
submit(safety_factor(bots, 100, size))
submit(next(t for t in count() if easter_egg(space(bots, t, size))))
