from aoc import get_input, submit

def get(grid, x, y, dx, dy, n):
    cs = []
    while 0 <= y < len(grid) and 0 <= x < len(grid[y]) and len(cs) < n:
        cs.append(grid[y][x])
        x += dx
        y += dy
    return ''.join(cs)

def search_xmas(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'X':
                for dx, dy in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
                    if get(grid, x + dx, y + dy, dx, dy, 3) == 'MAS':
                        count += 1
    return count

def search_x_mas(grid):
    count = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if grid[y][x] == 'A' and { grid[y-1][x-1], grid[y+1][x+1] } == { 'M', 'S' } and { grid[y-1][x+1], grid[y+1][x-1] } == { 'M', 'S' }:
                count += 1
    return count

grid = get_input(4).splitlines()
submit(search_xmas(grid))
submit(search_x_mas(grid))
