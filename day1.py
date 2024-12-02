from aoc import get_input, submit
from utils import table
from collections import Counter

def total_distance(xs, ys):
    return sum(abs(x - y) for x, y in zip(sorted(xs), sorted(ys)))

def similarity_score(xs, ys):
    x_counts = Counter(xs)
    y_counts = Counter(ys)
    return sum(n*x_counts[n]*y_counts[n] for n in x_counts.keys() & y_counts.keys())

pairs = table(get_input(1), int)
xs, ys = zip(*pairs)
submit(total_distance(xs, ys))
submit(similarity_score(xs, ys))
