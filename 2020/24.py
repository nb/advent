from collections import defaultdict

for f in ('sample24.txt', 'input24.txt'):
    print('\n***', f)
    lines = [line.strip() for line in open(f).readlines()]
    directions = 'e se sw w nw ne'.split(' ')
    offsets = [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]
    dir2off = dict(zip(directions, offsets))
    flipped = defaultdict(int)
    for line in lines:
        tile = (0, 0, 0)
        while line:
            for dir in directions:
                if line.startswith(dir):
                    tile = tuple(map(sum, zip(tile, dir2off[dir])))
                    line = line[len(dir):]
                    break
        flipped[tile] += 1
    print(sum(flipped[tile] % 2 == 1 for tile in flipped))
    blacks = {tile for tile in flipped if flipped[tile] % 2 == 1}
    for _ in range(100):
        new_black = set()
        neighbors = defaultdict(int)
        for tile in blacks:
            for offset in offsets:
                neighbors[tuple(map(sum, zip(tile, offset)))] += 1
        for tile, count in neighbors.items():
            if tile in blacks and count in (1, 2):
                new_black.add(tile)
            elif tile not in blacks and count == 2:
                new_black.add(tile)
        blacks = new_black
    print(len(blacks))