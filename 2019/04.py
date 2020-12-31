import re
import math
from itertools import chain, repeat
from functools import reduce, partial
from collections import defaultdict

start = 387638
end = 919123
n = 0
for x in range(start, end+1):
    digits = list(map(int, list(str(x))))
    same = False
    inc = True
    for a, b in zip(digits[:-1], digits[1:]):
        if a == b:
            same = True
        if a > b:
            inc = False
    if same and inc:
        n+=1
print(n)
n = 0
for x in range(start, end+1):
    digits = list(map(int, list(str(x))))
    same = False
    inc = True
    nsame = 1
    for a, b in zip(digits[:-1], digits[1:]):
        if a == b:
            nsame+=1
        else:
            if nsame == 2:
                same = True
            nsame = 1
        if a > b:
            inc = False
    if nsame == 2:
        same = True
    if same and inc:
        n+=1
print(n)