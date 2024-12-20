from aoc import get_input, submit
from utils import Vector2D
from collections import Counter

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

def find_cheats(grid, max_radius):
    path = find_path(grid)

    normal_times = {}
    for time, pos in enumerate(path):
        normal_times[pos] = time

    for start in path:
        for radius in range(2, max_radius + 1):
            for end in boundary(start, radius):
                if end in normal_times and normal_times[end] > normal_times[start]:
                    saving = (normal_times[end] - normal_times[start]) - radius
                    if saving > 0:
                        yield start, end, saving

def boundary(origin, radius):
    for i in range(1, radius + 1):
        yield Vector2D(origin.x + i, origin.y - radius + i)
        yield Vector2D(origin.x + radius - i, origin.y + i)
        yield Vector2D(origin.x - i, origin.y + radius - i)
        yield Vector2D(origin.x - radius + i, origin.y - i)

grid = get_input(20).splitlines()
# grid = '''###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############
# '''.splitlines()

# for start, end, saving in find_cheats(grid, 2):
#     if saving == 2:
#         new_grid = [list(row) for row in grid]
#         new_grid[start.y][start.x] = '0'
#         new_grid[end.y][end.x] = '2'
#         for row in new_grid:
#             print(''.join(row))
#         input()
# quit()

# counts = Counter()
# for start, end, saving in find_cheats(grid, 20):
#     counts[saving] += 1
# for saving in sorted(counts):
#     print('There are', counts[saving], 'cheats that save', saving, 'picoseconds.')

submit(sum(saving >= 100 for _, _, saving in find_cheats(grid, 2)))
submit(sum(saving >= 100 for _, _, saving in find_cheats(grid, 20)))
