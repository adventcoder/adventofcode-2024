from aoc import get_input, submit
from utils import Vector2D
from dataclasses import dataclass
from math import prod, lcm

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

size = Vector2D(101, 103)
bots = [parse_bot(line) for line in get_input(14).splitlines()]
submit(safety_factor(bots, 100, size))
submit(min(range(lcm(size.x, size.y)), key=lambda t: safety_factor(bots, t, size)))
