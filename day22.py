from aoc import get_input, submit
from utils import sliding_window
from collections import Counter

def evolve(secret):
    secret = prune(mix(secret, secret << 6))
    secret = prune(mix(secret, secret >> 5))
    secret = prune(mix(secret, secret << 11))
    return secret

def mix(a, b):
    return a ^ b

def prune(n):
    return n & ((1 << 24) - 1)

def prices(secret, n):
    yield secret % 10
    for _ in range(n):
        secret = evolve(secret)
        yield secret % 10

secrets = [int(line) for line in get_input(22).splitlines()]

total = 0
for secret in secrets:
    for _ in range(2000):
        secret = evolve(secret)
    total += secret
submit(total)

bananas = Counter()
for secret in secrets:
    seen = set()
    for window in sliding_window(prices(secret, 2000), 5):
        seq = ','.join(str(b - a) for a, b in sliding_window(window, 2))
        if seq not in seen:
            bananas[seq] += window[-1]
            seen.add(seq)
submit(max(bananas.values()))
