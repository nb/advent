for f in ('sample15.txt', 'input15.txt')[1:]:
    print('\n***', f)
    lines = [line.strip() for line in open(f).readlines()]
    numbers = list(map(int, lines[0].split(',')))
    spoken = {}
    SPOKEN = 30000000
    last = None
    for turn, n in enumerate(numbers, start=1):
        last = n
        spoken[last] = [turn]
    for turn in range(len(numbers) + 1, SPOKEN + 1):
        if (turn % 100000 == 0):
            print(int((turn/SPOKEN)*100))
        if not last in spoken or len(spoken[last]) != 2:
            last = 0
        else:
            last = spoken[last][1] - spoken[last][0]
        if last in spoken:
            spoken[last] = (spoken[last] + [turn])[-2:]
        else:
            spoken[last] = [turn]
    print(last)
