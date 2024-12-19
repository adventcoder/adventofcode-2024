from aoc import get_input, submit
from utils import Vector2D

dirs = [Vector2D(0, -1), Vector2D(1, 0), Vector2D(0, 1), Vector2D(-1, 0)]

def find_path(walls, end):
    closed = set()
    curr = [Vector2D(0, 0)]
    steps = 0
    while curr:
        next = []
        for pos in curr:
            if pos == end:
                return steps
            for dir in dirs:
                new_pos = pos + dir
                if 0 <= new_pos.x <= end.x and 0 <= new_pos.y <= end.y and new_pos not in walls and new_pos not in closed:
                    closed.add(new_pos)
                    next.append(new_pos)
        curr = next
        steps += 1
    return None

def bsearch(walls, end):
    lower = 1024        # INVARIANT: find_path(set(walls[:lower]), end) is not None
    upper = len(walls)  # INVARIANT: find_path(set(walls[:upper]), end) is None
    while upper - lower > 1:
        mid = (lower + upper) // 2
        if find_path(set(walls[:mid]), end) is None:
            upper = mid
        else:
            lower = mid
    return walls[lower]

walls = [Vector2D.parse(line) for line in get_input(18).splitlines()]
end = Vector2D(70, 70)
submit(find_path(set(walls[:1024]), end))
submit(bsearch(walls, end))
