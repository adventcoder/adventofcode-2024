from aoc import get_input, submit
from collections import defaultdict
from itertools import combinations
from utils import Vector2D

def in_bounds(grid, pos):
    return 0 <= pos.y < len(grid) and 0 <= pos.x < len(grid[pos.y])

def find_antennae(grid):
    antennae = defaultdict(set)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c != '.':
                antennae[c].add(Vector2D(x, y))
    return antennae

def antinodes1(grid, antennae):
    antinodes = set()
    for group in antennae.values():
        for a, b in combinations(group, 2):
            diff = b - a
            for antinode in (a - diff, b + diff):
                if in_bounds(grid, antinode):
                    antinodes.add(antinode)
    return antinodes

def antinodes2(grid, antennae):
    antinodes = set()
    for group in antennae.values():
        for a, b in combinations(group, 2):
            diff = b - a
            while in_bounds(grid, a):
                antinodes.add(a)
                a -= diff
            while in_bounds(grid, b):
                antinodes.add(b)
                b += diff
    return antinodes

grid = get_input(8).splitlines()
antennae = find_antennae(grid)
submit(len(antinodes1(grid, antennae)))
submit(len(antinodes2(grid, antennae)))
