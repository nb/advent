import math

for f in ('sample13.txt', 'input13.txt'):
    print(f)
    lines = [line.strip() for line in open(f).readlines()]
    earliest_ts = int(lines[0])
    ids = [int(id) for id in lines[1].split(',') if id != 'x']
    id, wait = min(((id, id - earliest_ts % id)
                    for id in ids), key=lambda value: value[1])
    print(id*wait)

    mods = [(int(id) - i) % int(id)
            for i, id in enumerate(lines[1].split(',')) if id != 'x']
    # Chinese remainder theorem
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    N = math.prod(ids)
    print(sum(mod * pow(N//n, -1, n) * (N // n)
              for n, mod in zip(ids, mods)) % N)
