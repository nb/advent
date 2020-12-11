from collections import Counter
from itertools import chain

dirs = [(1, 0), (1, -1), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]


def outside(seats, a, b):
    return a < 0 or a >= len(seats) or b < 0 or b >= len(seats[0])


def empty(seats, a, b, dir):
    a, b = a + dir[0], b + dir[1]
    return outside(seats, a, b) or seats[a][b] != '#'


def occupied(seats, a, b, dir):
    a, b = a + dir[0], b + dir[1]
    return (not outside(seats, a, b)) and seats[a][b] == '#'


def sees_occupied(seats, a, b, dir):
    a, b = a + dir[0], b + dir[1]
    if a < 0 or a >= len(seats) or b < 0 or b >= len(seats[0]):
        return False
    if seats[a][b] == 'L':
        return False
    if seats[a][b] == '#':
        return True
    if seats[a][b] == '.':
        return sees_occupied(seats, a, b, dir)


def count_occupied(original_seats, should_occupy, should_release):
    seats = [row[:] for row in original_seats[:]]
    while True:
        new_seats = [row[:] for row in seats[:]]
        changed = 0
        for r, row in enumerate(seats):
            for i, seat in enumerate(row):
                if seat == 'L' and should_occupy(seats, r, i):
                    new_seats[r][i] = '#'
                    changed = changed + 1
                if seat == '#' and should_release(seats, r, i):
                    new_seats[r][i] = 'L'
                    changed = changed + 1
        if changed == 0:
            break
        seats = new_seats
    return Counter(chain(*seats))['#']


for f in ('sample11.txt', 'input11.txt'):
    seats = [list(line.strip()) for line in open(f).readlines()]
    print(f)
    print(count_occupied(seats, lambda seats, r, i: all(empty(seats, r, i, dir)
                                                        for dir in dirs), lambda seats, r, i: sum(occupied(seats, r, i, dir) for dir in dirs) >= 4))
    print(count_occupied(seats, lambda seats, r, i: not any(sees_occupied(seats, r, i, dir)
                                                            for dir in dirs), lambda seats, r, i: sum(sees_occupied(seats, r, i, dir) for dir in dirs) >= 5))
