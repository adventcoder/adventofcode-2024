from aoc import get_input, submit
from functools import cache

sections = get_input(19).split('\n\n')
towels = sections[0].split(', ')
designs = sections[1].splitlines()

@cache
def ways(design):
    if design == '':
        return 1
    total = 0
    for towel in towels:
        if design.startswith(towel):
            total += ways(design[len(towel):])
    return total

submit(sum(ways(design) > 0 for design in designs))
submit(sum(ways(design) for design in designs))
