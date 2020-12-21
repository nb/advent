import re
from collections import defaultdict

for f in ('sample21.txt', 'input21.txt'):
    print('\n***', f)
    lines = [line.strip() for line in open(f).readlines()]
    possible_ingredients = {}
    allergen_from_ingredient = {}
    count_per_ingredient = defaultdict(lambda: 0)
    for line in lines:
        m = re.match(r'(.*) \(contains (.*)\)', line)
        ingredients = set(m[1].split(' '))
        allergens = m[2].split(', ')
        for ingredient in ingredients:
            count_per_ingredient[ingredient] += 1
        for allergen in allergens:
            if allergen in possible_ingredients:
                possible_ingredients[allergen] = possible_ingredients[allergen] & ingredients
            else:
                possible_ingredients[allergen] = set(ingredients)
    while True:
        ingredient = None
        for a in possible_ingredients:
            if len(possible_ingredients[a]) == 1:
                ingredient = next(iter(possible_ingredients[a]))
                allergen_from_ingredient[ingredient] = a
                break
        if ingredient == None:
            break
        for x in possible_ingredients:
            possible_ingredients[x].discard(ingredient)
    free_ingredients = set(count_per_ingredient.keys()) - set(allergen_from_ingredient.keys())
    print(sum(count_per_ingredient[x] for x in free_ingredients))
    sorted_by_allergen = sorted(allergen_from_ingredient, key=lambda k: allergen_from_ingredient[k])
    print(','.join(sorted_by_allergen))