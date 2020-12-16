import math
import re
from itertools import chain
from collections import defaultdict


def matches_rule(n, rule):
    a, b, c, d = rule
    return (n >= a and n <= b) or (n >= c and n <= d)


parts = open('input16.txt').read().split('\n\n')
rules = [[int(x) for x in re.findall(r'(\d+)', line)]
         for line in parts[0].split('\n')]
my = [int(x) for x in parts[1].split('\n')[1].split(',')]
nearby = [[int(x) for x in line.split(',')]
          for line in parts[2].split('\n')[1:] if line != '']

print(sum(x for x in chain(*nearby) if all(not matches_rule(x, rule)
                                           for rule in rules)))
impossible_positions = defaultdict(set)
for ticket in nearby:
    if any(all(not matches_rule(x, rule) for rule in rules) for x in ticket):
        continue
    for i, x in enumerate(ticket):
        for ri, rule in enumerate(rules):
            if not matches_rule(x, rule):
                impossible_positions[ri].add(i)
found = {}
while len(found) < 6:
    for ri in impossible_positions:
        if len(impossible_positions[ri]) == 19:
            i = list(set(range(20)) - impossible_positions[ri])[0]
            if ri < 6:
                found[ri] = i
            for k in impossible_positions:
                impossible_positions[k].add(i)
print(math.prod(my[found[ri]] for ri in found))
