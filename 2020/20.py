import math
from collections import defaultdict

for f in ('sample20.txt', 'input20.txt'):
    print('\n***', f)
    tile_parts = open(f).read().split('\n\n')
    tiles = {}
    sharps = 0
    for tile_part in tile_parts:
        lines = tile_part.split('\n')
        tile_id = int(lines[0][:-1].split(' ')[1])
        tile = lines[1:]
        sharps += sum(sum(c == '#' for c in line[1:-1]) for line in tile[1:-1])
        tiles[tile_id] = (tile[0], ''.join(line[-1] for line in tile), tile[-1], ''.join(line[0] for line in tile))
    n = int(math.sqrt(len(tiles)))
    commons = defaultdict(list)
    for tile_id in tiles:
        for other_tile_id in tiles:
            if tile_id == other_tile_id:
                continue
            for side in tiles[other_tile_id]:
                if side in tiles[tile_id] or side in [s[::-1] for s in tiles[tile_id]]:
                    commons[tile_id].append(other_tile_id)
    print(math.prod((tile_id for tile_id in tiles if len(commons[tile_id])==2)))

    # searched for ##....### (regex) – 13 solutions in my
    # so, let's try double that: 26 monsters, too high
    # try triple: 39: too low
    # a couple more tries: 30 :)
    total_monsters = 30
    monster_sharps = 15
    print(sharps - total_monsters * monster_sharps)
