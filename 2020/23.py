import re
import math
from itertools import chain, repeat
from functools import reduce, partial
from collections import defaultdict

for f in ('389125467', '398254716'):
    cups = list(map(int, list(f)))
    print(list(cups))
    n = len(cups)
    c = 0
    mi, ma = min(cups), max(cups)
    for i in range(100):
        x, y, z = cups[(c+1)%n], cups[(c+2)%n], cups[(c+3)%n]
        oc = cups[c]
        d = cups[c] - 1
        cups = [i for j, i in enumerate(cups) if j not in ((c+1)%n, (c+2)%n, (c+3)%n)]
        while True:
            if d in cups:
                break
            if d in (x, y, z):
                d -= 1
            if d < mi:
                d = ma
        di = cups.index(d)
        cups = cups[:(di+1)] + [x, y, z] + cups[(di+1):100]
        c = (cups.index(oc)+1)%n

    i1 = cups.index(1)
    print(''.join(map(str, (cups*2)[i1+1:i1+9])))
        
