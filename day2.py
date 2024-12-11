from aoc import get_input, submit
from utils import table, sliding_window

def safe(record):
    increasing = all(a < b for a, b in sliding_window(record, 2))
    decreasing = all(a > b for a, b in sliding_window(record, 2))
    diffs = all(1 <= abs(b - a) <= 3 for a, b in sliding_window(record, 2))
    return (increasing or decreasing) and diffs

def safe_with_dampener(record):
    #TODO: brute force
    return any(safe(record[:i] + record[i+1:]) for i in range(len(record)))

records = table(get_input(2), int)
submit(sum(safe(record) for record in records))
submit(sum(safe_with_dampener(record) for record in records))
