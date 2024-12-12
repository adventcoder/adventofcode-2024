from aoc import get_input, submit

N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)

def visit(grid, x, y):
    c = grid[y][x]
    region = set()
    region.add((x, y))
    edges = 0
    sides = 0
    queue = [(x, y)]
    while queue:
        x, y = queue.pop()
        for dx, dy in [N, E, S, W]:
            nx, ny = x + dx, y + dy
            if include(grid, nx, ny, c):
                if (nx, ny) not in region:
                    region.add((nx, ny))
                    queue.append((nx, ny))
            else:
                edges += 1
        # The number of sides and corners are the same.
        #
        # A corner either looks like this (exterior):
        #
        # X.
        # AX
        #
        # Or this (interior):
        #
        # AX
        # AA
        #
        for (dx1, dy1), (dx2, dy2) in [(N, E), (E, S), (S, W), (W, N)]:
            if (not include(grid, x+dx1, y+dy1, c) and not include(grid, x+dx2, y+dy2, c)) or (include(grid, x+dx1, y+dy1, c) and include(grid, x+dx2, y+dy2, c) and not include(grid, x+dx1+dx2, y+dy1+dy2, c)):
                sides += 1
    return region, edges, sides

def include(grid, x, y, c):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] == c

input = get_input(12)
grid = input.splitlines()

visited = set()
total_price1 = 0
total_price2 = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if (x, y) not in visited:
            region, edges, sides = visit(grid, x, y)
            visited.update(region)
            total_price1 += len(region)*edges
            total_price2 += len(region)*sides
submit(total_price1)
submit(total_price2)
