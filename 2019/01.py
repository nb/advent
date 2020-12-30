import math
def fuel(mass, recurse=True):
    f = math.floor(mass/3) - 2
    if f < 0:
        return 0
    return f + fuel(f) if recurse else f

for f in ('sample01.txt', 'input01.txt'):
    print('\n***', f)
    lines = open(f).readlines()
    for recurse in (False, True):
        print(sum(fuel(int(line.strip()), recurse) for line in lines))
