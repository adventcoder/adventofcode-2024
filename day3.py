from aoc import get_input, submit
import re

def eval(s):
    return sum(int(a)*int(b) for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', s))

def eval_with_conditionals(s):
    total = 0
    enabled = True
    for s in re.findall(r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)', s):
        if s.startswith('don\'t'):
            enabled = False
        elif s.startswith('do'):
            enabled = True
        elif s.startswith('mul'):
            if enabled:
                a, b = s[4:-1].split(',')
                total += int(a) * int(b)
    return total

input = get_input(3)
submit(eval(input))
submit(eval_with_conditionals(input))
