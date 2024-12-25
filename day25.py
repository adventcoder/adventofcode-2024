from aoc import get_input, submit

locks = []
keys = []

for section in get_input(25).split('\n\n'):
    grid = section.splitlines()
    mask = 0
    for row in grid[1:-1]:
        for c in row:
            mask = (mask << 1) | int(c == '#')
    if '#' in grid[0]:
        locks.append(mask)
    if '#' in grid[-1]:
        keys.append(mask)

def fits(lock, key):
    return lock & key == 0

submit(sum(fits(lock, key) for lock in locks for key in keys))
