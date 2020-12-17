from itertools import product, chain
from operator import add

def life(actives, dimensions):
    offsets = set(product((0, 1, -1), repeat=dimensions)) - set([(0,) * dimensions])
    actives = set(cell + (0,) * (dimensions-2) for cell in actives)
    neighbors = lambda cell: (tuple(map(add, cell, offset)) for offset in offsets)
    active_neighbors_count = lambda cell: sum(n in actives for n in neighbors(cell))
    inactive_neighbors = lambda cell: (n for n in neighbors(cell) if n not in actives)
    all_inactive_neighbors = lambda: set(chain(*(inactive_neighbors(cell) for cell in actives)))
    for _ in range(6):
        rule_active = set(cell for cell in actives if active_neighbors_count(cell) in (2, 3))
        rule_resurrect = set(cell for cell in all_inactive_neighbors() if active_neighbors_count(cell) == 3)
        actives = rule_active | rule_resurrect
    return actives

for f in ('sample17.txt', 'input17.txt'):
    print('\n***', f)
    lines = [line.strip() for line in open(f).readlines()]
    actives = [(x, y) for x, line in enumerate(lines) for y, c in enumerate(line) if c == '#']
    print(len(life(actives, 3)))
    print(len(life(actives, 4)))