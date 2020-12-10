import re


def rule_from_line(line):
    rule = {}
    outer, inner = line.strip()[:-1].split(' bags contain ')
    rule['outer'] = outer
    if inner == 'no other bags':
        rule['inners'] = {}
    else:
        rule['inners'] = {color: int(count) for (count, color) in re.findall(
            r'(\d+) (\w+ \w+) bags?', inner)}
    return rule


def bags_from_rules(rules):
    bags = {rule['outer']: {'includes': rule['inners'], 'can-be-in': set()}
            for rule in rules}
    for bag in bags:
        for inner in bags[bag]['includes']:
            bags[inner]['can-be-in'].add(bag)
    return bags


def can_be_in(bags):
    possible = {}

    def possibles(color):
        if color in possible:
            return possible[color]
        possible[color] = set().union(
            *map(possibles, bags[color]['can-be-in'])).union(bags[color]['can-be-in'])
        return possible[color]

    return possibles('shiny gold')


def includes(bags):
    counts = {}

    def count(color):
        if color in counts:
            return counts[color]
        counts[color] = sum((1+count(inner))*bags[color]['includes'][inner]
                            for inner in bags[color]['includes'])
        return counts[color]
    return count('shiny gold')


for f in ('sample7.txt', 'sample7-2.txt', 'input7.txt'):
    bags = bags_from_rules(map(rule_from_line, open(f).readlines()))
    print(f)
    print('can be in', len(can_be_in(bags)))
    print('includes', includes(bags))
