for f in ('sample12.txt', 'input12.txt'):
    print(f)
    commands = [(line.strip()[0], int(line.strip()[1:]))
                for line in open(f).readlines()]
    dirs = ('E', 'N', 'W', 'S')
    offsets = dict(zip(dirs, ((1, 0), (0, 1), (-1, 0), (0, -1))))

    def move(x, y, dir, dist):
        return x + (dist*offsets[dir][0]), y + (dist*offsets[dir][1])

    x, y, current_dir = 0, 0, 'E'
    for action, dist in commands:
        if action in dirs:
            x, y = move(x, y, action, dist)
        if action == 'F':
            x, y = move(x, y, current_dir, dist)
        if action in ('L', 'R'):
            moves = dist // 90 * (1 if 'L' == action else -1)
            current_dir = dirs[(dirs.index(current_dir) + moves) % 4]
    print(abs(x) + abs(y))

    x, y, wx, wy = 0, 0, 10, 1
    for action, dist in commands:
        if action in dirs:
            wx, wy = move(wx, wy, action, dist)
        if action == 'F':
            x, y = x + dist * wx, y + dist * wy
        if action in ('L', 'R'):
            moves = dist // 90
            for _ in range(moves):
                wx, wy = wy, wx
                wx = wx * (1 if 'R' == action else -1)
                wy = wy * (1 if 'L' == action else -1)
    print(abs(x) + abs(y))
