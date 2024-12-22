from aoc import get_input, submit
from functools import cache
from utils import sliding_window

numpad = '789\n456\n123\n 0A'.splitlines()
dirpad = ' ^A\n<v>'.splitlines()

def find_paths(start, end, numeric):
    #TODO: cleanup
    keypad = numpad if numeric else dirpad
    for y, row in enumerate(keypad):
        for x, c in enumerate(row):
            if c == start:
                start_x, start_y = x, y
            if c == end:
                end_x, end_y = x, y
    def recur(x, y):
        if x == end_x and y == end_y:
            yield 'A'
        else:
            if x < end_x and keypad[y][x + 1] != ' ':
                for path in recur(x + 1, y):
                    yield '>' + path
            elif x > end_x and keypad[y][x - 1] != ' ':
                for path in recur(x - 1, y):
                    yield '<' + path
            if y < end_y and keypad[y + 1][x] != ' ':
                for path in recur(x, y + 1):
                    yield 'v' + path
            elif y > end_y and keypad[y - 1][x] != ' ':
                for path in recur(x, y - 1):
                    yield '^' + path
    return recur(start_x, start_y)

def total_path_length(path, expansions, numeric):
    return sum(path_length(start, end, expansions, numeric) for start, end in sliding_window('A' + path, 2))

@cache
def path_length(start, end, expansions, numeric):
    if expansions == 0:
        return 1
    return min(total_path_length(path, expansions - 1, False) for path in find_paths(start, end, numeric))

def complexity(code, expansions):
    return int(code[:-1]) * total_path_length(code, expansions, True)

codes = get_input(21).splitlines()
submit(sum(complexity(code, 3) for code in codes))
submit(sum(complexity(code, 26) for code in codes))
