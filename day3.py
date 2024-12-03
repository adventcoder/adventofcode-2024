from aoc import get_input, submit
import re

def eval(s):
    return sum(int(a)*int(b) for a, b in re.findall(r'mul\(([0-9]+),([0-9]+)\)', s))

def eval_with_conditionals(s):
    return eval(re.sub(r"don't\(\)(.*?)do\(\)", '', s))

input = get_input(3)
submit(eval(input))
submit(eval_with_conditionals(input))
