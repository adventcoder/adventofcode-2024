from aoc import get_input
from collections import Counter

xs, ys = zip(*[map(int, line.split()) for line in get_input(1).splitlines()])

print('1.', sum(abs(x - y) for x, y in zip(sorted(xs), sorted(ys))))

x_counts = Counter(xs)
y_counts = Counter(ys)
print('2.', sum(n*x_counts[n]*y_counts[n] for n in x_counts.keys() & y_counts.keys()))
