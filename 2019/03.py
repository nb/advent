def points(wire):
    x, y = 0, 0
    r = set()
    steps = {}
    step = 0
    def add(x, y):
        r.add((x, y))
        if not (x, y) in steps:
            steps[(x, y)] = step
    for d, n in wire:
        if d == 'R':
            for i in range(x+1, x+n+1):
                step += 1
                add(i, y)
            x += n
        if d == 'L':
            for i in range(x-1, x-n-1, -1):
                step += 1
                add(i, y)
            x -= n
        if d == 'U':
            for i in range(y+1, y+n+1):
                step += 1
                add(x, i)
            y += n
        if d == 'D':
            for i in range(y-1, y-n-1, -1):
                step += 1
                add(x, i)
            y -= n
    return r, steps

for f in ('sample03.txt', 'sample03-2.txt', 'input03.txt')[:3]:
    print('\n***', f)
    lines = [line.strip() for line in open(f).readlines()]
    wires = [[(w[0], int(w[1:])) for w in lines[0].split(',')], [(w[0], int(w[1:])) for w in lines[1].split(',')]]
    p0, s0 = points(wires[0])
    p1, s1 = points(wires[1])
    common = p0 & p1
    #print(s0, s1, common)
    print(min(abs(x)+abs(y) for x, y in common if (x,y) != (0,0)))
    print(min(s0[(x,y)] + s1[(x, y)] for x, y in common if (x,y) != (0,0)))

