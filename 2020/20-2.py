
import math
from collections import defaultdict

def rotations(t):
    tt = t * 2
    yield t
    for i in range(3):
        n = tt[i+1:i+5]
        yield [n[0], n[1][::-1], n[2], n[3][::-1]]

def flips(t):
    yield t
    yield [t[0][::-1], t[3], t[2][::-1], t[1]]
    yield [t[2], t[1][::-1], t[0], t[3][::-1]]
    yield [t[0][::-1], t[1], t[2][::-1], t[3]]

downs = defaultdict(list)
rights = defaultdict(list)

def find(to_now, tile_ids):
    i = len(to_now)
    if len(found) > 0:
        return
    if i >= (n*n):
        found.append(to_now)
        return
    if i % n == 0:
        next_tiles = downs[tuple(to_now[i-n][:3])]
    elif i > 0:
        next_tiles = rights[tuple(to_now[i-1][:3])]
    for option in next_tiles:
        new_tile_id, _, _, new_f = option
        if new_tile_id in tile_ids:
            continue
        c = []
        if i % n != 0: # left
            c.append(to_now[i-1][3][1] == new_f[3])
        if i >= n: # up
            c.append(to_now[i-n][3][2] == new_f[0])
        if all(c):
            find(to_now + [option], tile_ids | {new_tile_id})

for f in ('sample20.txt', 'input20.txt'):
    print('\n***', f)
    tile_parts = open(f).read().split('\n\n')
    tiles = {}
    for tile_part in tile_parts:
        lines = tile_part.split('\n')
        tile_id = int(lines[0][:-1].split(' ')[1])
        tile = lines[1:]
        tiles[tile_id] = (tile[0], ''.join(line[-1] for line in tile), tile[-1], ''.join(line[0] for line in tile))
    n = int(math.sqrt(len(tiles)))
    found = []
    for tile_id, tile in tiles.items():
        for ri, r in enumerate(rotations(tile)):
            for fi, f in enumerate(flips(r)):
                for new_tile_id, new_tile in tiles.items():
                    for new_ri, new_r in enumerate(rotations(new_tile)):
                        for new_fi, new_f in enumerate(flips(new_r)):
                            if tile_id == new_tile_id:
                                continue
                            if (f[2] == new_f[0]): # can down?
                                downs[(tile_id, ri, fi)].append((new_tile_id, new_ri, new_fi, new_f))
                            if (f[1] == new_f[3]): # can right
                                rights[(tile_id, ri, fi)].append((new_tile_id, new_ri, new_fi, new_f))
    for tile_id, tile in tiles.items():
        for ri, r in enumerate(rotations(tile)):
            for fi, f in enumerate(flips(r)):
                if (tile_id, ri, fi) in rights:
                    find([(tile_id, ri, fi, f)], set([tile_id]))
    found = found[0]
    print(found[0][0] * found[n-1][0] * found[-1][0] * found[-n][0])