from aoc import get_input, submit

def step(x, y, d):
    match d:
        case '^':
            return x, y - 1
        case '>':
            return x + 1, y
        case '<':
            return x - 1, y
        case 'v':
            return x, y + 1

def move_bot(grid, d):
    x, y = find_bot(grid)
    if can_move(grid, x, y, d):
        move(grid, x, y, d)

def find_bot(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '@':
                return x, y

def move(grid, x, y, d):
    nx, ny = step(x, y, d)
    if grid[y][x] in '@O' or (grid[y][x] in '[]' and d in '<>'):
        move(grid, nx, ny, d)
        grid[ny][nx] = grid[y][x]
        grid[y][x] = '.'
    if grid[y][x] in '[]' and d in '^v':
        other_x = x + 1 if grid[y][x] == '[' else x - 1
        other_nx = nx + 1 if grid[y][x] == '[' else nx - 1
        move(grid, nx, ny, d)
        move(grid, other_nx, ny, d)
        grid[ny][nx] = grid[y][x]
        grid[ny][other_nx] = grid[y][other_x]
        grid[y][x] = '.'
        grid[y][other_x] = '.'
    assert grid[y][x] == '.'

def can_move(grid, x, y, d):
    if grid[y][x] == '.':
        return True
    if grid[y][x] == '#':
        return False
    if grid[y][x] in '@O' or (grid[y][x] in '[]' and d in '<>'):
        return can_move(grid, *step(x, y, d), d)
    if grid[y][x] in '[]' and d in '^v':
        other_x = x + 1 if grid[y][x] == '[' else x - 1
        return can_move(grid, *step(x, y, d), d) and can_move(grid, *step(other_x, y, d), d)
    assert False

def gps(grid):
    total = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'O' or c == '[':
                total += x + 100*y
    return total

def widen(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for c in row:
            match c:
                case '#' | '.':
                    new_row.extend([c, c])
                case 'O':
                    new_row.extend(['[', ']'])
                case '@':
                    new_row.extend(['@', '.'])
        new_grid.append(new_row)
    return new_grid

input = get_input(15)
sections = input.split('\n\n')
grid = [list(line) for line in sections[0].splitlines()]
wide_grid = widen(grid)
dirs = ''.join(sections[1].splitlines())

for d in dirs:
    move_bot(grid, d)
submit(gps(grid))

for d in dirs:
    move_bot(wide_grid, d)
submit(gps(wide_grid))
