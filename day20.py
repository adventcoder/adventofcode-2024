from aoc import get_input, submit
from utils import Vector2D

def find(grid, target):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == target:
                return Vector2D(x, y)

grid = get_input(20).splitlines()
grid = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''.splitlines()
