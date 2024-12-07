from aoc import get_input, submit
from collections import defaultdict
from functools import cmp_to_key
from utils import sliding_window

def parse(input):
    sections = input.split("\n\n")

    rules = defaultdict(set)
    for line in sections[0].splitlines():
        before, after = line.split('|')
        rules[int(after)].add(int(before))

    updates = []
    for line in sections[1].splitlines():
        updates.append([int(page) for page in line.split(',')])

    return rules, updates

def in_order(update, rules):
    return all(a in rules[b] for a, b in sliding_window(update, 2))

def sort_by_rules(update, rules):
    def cmp(a, b):
        return 1 if a in rules[b] else -1
    return sorted(update, key=cmp_to_key(cmp))

def middle(update):
    return update[len(update) // 2]

rules, updates = parse(get_input(5))
submit(sum(middle(update) for update in updates if in_order(update, rules)))
submit(sum(middle(sort_by_rules(update, rules)) for update in updates if not in_order(update, rules)))
