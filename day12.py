from aoc import get_input, submit

#TODO: wash me

def visit(grid, x, y):
    up_edges = []
    down_edges = []
    right_edges = []
    left_edges = []
    region = set()
    region.add((x, y))
    queue = [(x, y)]
    while queue:
        x, y = queue.pop()
        for nx, ny in [(x,y-1), (x+1,y), (x,y+1), (x-1,y)]:
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] == grid[y][x]:
                if (nx, ny) not in region:
                    region.add((nx, ny))
                    queue.append((nx, ny))
            else:
                dx = nx - x
                dy = ny - y
                if dy == -1:
                    up_edges.append((y, x, x + 1))
                if dy == 1:
                    down_edges.append((y + 1, x, x + 1))
                if dx == -1:
                    left_edges.append((x, y, y + 1))
                if dx == 1:
                    right_edges.append((x + 1, y, y + 1))
    return region, up_edges, down_edges, right_edges, left_edges

def join(edges):
    intervals = {}
    for x, y0, y1 in edges:
        if x not in intervals:
            intervals[x] = [(y0, y1)]
        else:
            merge(intervals[x], (y0, y1))
    return [(x, y0, y1) for x in intervals for y0, y1 in intervals[x]]

def merge(intervals, new_interval):
    before_i = None
    after_i = None
    for i, interval in enumerate(intervals):
        if interval[1] == new_interval[0]:
            before_i = i
        if interval[0] == new_interval[1]:
            after_i = i
    if before_i is None and after_i is None:
        return intervals.append(new_interval)
    if before_i is None and after_i is not None:
        after = intervals.pop(after_i)
        intervals.append((new_interval[0], after[1]))
    if before_i is not None and after_i is None:
        before = intervals.pop(before_i)
        intervals.append((before[0], new_interval[1]))
    if before_i is not None and after_i is not None:
        if before_i < after_i:
            after = intervals.pop(after_i)
            before = intervals.pop(before_i)
        else:
            before = intervals.pop(before_i)
            after = intervals.pop(after_i)
        return intervals.append((before[0], after[1]))

input = get_input(12)
grid = input.splitlines()

visited = set()
total_price1 = 0
total_price2 = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if (x, y) not in visited:
            region, up_edges, down_edges, right_edges, left_edges = visit(grid, x, y)
            visited.update(region)
            total_price1 += len(region)*(len(up_edges) + len(down_edges) + len(right_edges) + len(left_edges))
            total_price2 += len(region)*(len(join(up_edges)) + len(join(down_edges)) + len(join(right_edges)) + len(join(left_edges)))
submit(total_price1)
submit(total_price2)
