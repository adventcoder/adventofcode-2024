from aoc import get_input, submit

locks = []
keys = []

for section in get_input(25).split('\n\n'):
    grid = section.splitlines()
    if '#' in grid[0]:
        lock = []
        for x in range(5):
            y = 0
            while grid[y+1][x] == '#':
                y += 1
            lock.append(y)
        locks.append(lock)
    elif '#' in grid[-1]:
        key = []
        for x in range(5):
            y = 0
            while grid[5-y][x] == '#':
                y += 1
            key.append(y)
        keys.append(key)

def fits(lock, key):
    return all(a + b <= 5 for a, b in zip(lock, key))

submit(sum(fits(lock, key) for lock in locks for key in keys))
