from aoc import get_input, submit
from functools import cache

@cache
def count(n, blinks):
    if blinks == 0:
        return 1

    if n == 0:
        return count(1, blinks - 1)

    s = str(n)
    if len(s) % 2 == 0:
        l = int(s[:len(s)//2])
        r = int(s[len(s)//2:])
        return count(l, blinks - 1) + count(r, blinks - 1)

    return count(n * 2024, blinks - 1)


input = get_input(11)
stones = list(map(int, input.split()))
submit(sum(count(n, 25) for n in stones))
submit(sum(count(n, 75) for n in stones))
