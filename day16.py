from aoc import get_input, submit
from utils import Vector2D
import heapq

def find_best_paths(grid):
    start_pos = find_pos(grid, 'S')
    end_pos = find_pos(grid, 'E')
    start = (start_pos, Vector2D(1, 0))
    best_scores = { start: 0 }
    pred = { start: {} }
    queue = [(0, start)]
    best_score = None
    tiles = set()
    while queue:
        score, state = heapq.heappop(queue)
        if score > best_scores[state]:
            continue
        if best_score is not None and score > best_score:
            break
        if state[0] == end_pos:
            best_score = score
            backtrack(state, pred, tiles)
        else:
            for new_state, delta in step(grid, state):
                new_score = score + delta
                if new_state not in best_scores or new_score < best_scores[new_state]:
                    best_scores[new_state] = new_score
                    pred[new_state] = { state }
                    heapq.heappush(queue, (new_score, new_state))
                elif new_state in best_scores and new_score == best_scores[new_state]:
                    pred[new_state].add(state)
    return best_score, tiles

def find_pos(grid, target):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == target:
                return Vector2D(x, y)

def step(grid, state):
    pos, dir = state
    new_pos = pos + dir
    if grid[new_pos.y][new_pos.x] != '#':
        yield (new_pos, dir), 1
    yield (pos, dir.rot90(-1)), 1000
    yield (pos, dir.rot90(1)), 1000

def backtrack(state, pred, tiles):
    tiles.add(state[0])
    for prev_state in pred[state]:
        backtrack(prev_state, pred, tiles)

grid = [list(line) for line in get_input(16).splitlines()]
best_score, tiles = find_best_paths(grid)
# for tile in tiles:
#     grid[tile.y][tile.x] = 'O'
# for row in grid:
#     print(''.join(row))
submit(best_score)
submit(len(tiles))
