import math


def count(area, right, down):
    width = len(area[0])
    needed_width = len(area)*right*down
    new_area = [row*(math.ceil(needed_width/width)) for row in area]
    x, y, trees = 0, 0, 0
    while True:
        x, y = x + right, y + down
        if y >= len(new_area):
            break
        if new_area[y][x] == '#':
            trees = trees + 1
    return trees


area = [line.strip() for line in open('input3.txt').readlines()]
counts = [count(area, right, down)
          for (right, down) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]
print(counts)
