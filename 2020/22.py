def game(cards1, cards2, recursive):
    turns = set()
    while cards1 and cards2:
        key = (tuple(cards1), tuple(cards2))
        if key in turns:
            return (True, cards1)
        turns.add(key)
        c1, c2 = cards1.pop(0), cards2.pop(0)
        winner = c1 > c2
        if recursive and len(cards1) >= c1 and len(cards2) >= c2:
            winner, _ = game(cards1[:c1][:], cards2[:c2][:], recursive=True)
        if winner:
            cards1 += [c1, c2]
        else:
            cards2 += [c2, c1]
    return (True, cards1) if cards1 else (False, cards2)

for f in ('sample22.txt', 'input22.txt'):
    print('\n***', f)
    p1, p2 = open(f).read().split('\n\n')
    cards1 = [int(x) for x in p1.split('\n')[1:]]
    cards2 = [int(x) for x in p2.split('\n')[1:]]

    for recursive in (False, True):
        _, cards = game(cards1[:], cards2[:], recursive)
        print(sum(a*i for a, i in zip(cards, range(len(cards), 0, -1))))