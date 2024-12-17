from aoc import get_input, submit
from utils import Vector2D
import heapq
from math import inf

def find_pos(grid, target):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == target:
                return Vector2D(x, y)

def step(grid, pos, dir):
    for i in (-1, 0, 1):
        new_dir = dir.rot90(i)
        new_pos = pos + new_dir
        if grid[new_pos.y][new_pos.x] != '#':
            yield new_pos, new_dir, abs(i)*1000 + 1

def find_best_path(grid):
    start_pos = find_pos(grid, 'S')
    start_dir = Vector2D(0, 1)
    end_pos = find_pos(grid, 'E')
    best_scores = { (start_pos, start_dir): 0 }
    queue = [(0, start_pos, start_dir, (start_pos, ))]
    while queue:
        score, pos, dir, path = heapq.heappop(queue)
        # this check is needed since we don't remove from the heap when we find better paths
        if score > best_scores[(pos, dir)]:
            continue
        if pos == end_pos:
            # new_grid = [list(row) for row in grid]
            # for pos in path:
            #     new_grid[pos.y][pos.x] = 'O'
            # for row in new_grid:
            #     print(''.join(row))
            return score
        for new_pos, new_dir, delta in step(grid, pos, dir):
            new_score = score + delta
            new_path = path + (new_pos, )
            if new_score < best_scores.get((new_pos, new_dir), inf):
                best_scores[(new_pos, new_dir)] = new_score
                heapq.heappush(queue, (new_score, new_pos, new_dir, new_path))

grid = get_input(16).splitlines()
submit(find_best_path(grid))
