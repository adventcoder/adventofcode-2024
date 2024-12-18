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

walls = [Vector2D.parse(line) for line in get_input(18).splitlines()]
end = Vector2D(70, 70)
submit(find_path(set(walls[:1024]), end))
submit(next(str(walls[n-1]) for n in range(len(walls)) if find_path(set(walls[:n]), end) is None))
