from aoc import get_input, submit

def match(grid, x, y, dx, dy, target):
    s = ''.join(grid[y + i*dy][x + i*dx] for i in range(len(target)))
    return s == target or s[::-1] == target

def search(grid, s):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y]) - len(s) + 1):
            count += match(grid, x, y, 1, 0, s)
    for y in range(len(grid) - len(s) + 1):
        for x in range(len(grid[y])):
            count += match(grid, x, y, 0, 1, s)
    for y in range(len(grid) - len(s) + 1):
        for x in range(len(grid[y]) - len(s) + 1):
            count += match(grid, x, y, 1, 1, s)
            count += match(grid, x + len(s) - 1, y, -1, 1, s)
    return count

def search_x(grid, s):
    count = 0
    for y in range(len(grid) - len(s) + 1):
        for x in range(len(grid[y]) - len(s) + 1):
            count += match(grid, x, y, 1, 1, s) and match(grid, x + len(s) - 1, y, -1, 1, s)
    return count


grid = get_input(4).splitlines()
submit(search(grid, 'XMAS'))
submit(search_x(grid, 'MAS'))
