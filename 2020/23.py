class Node():
    __slots__ = ['v', 'r', 'd']
    def __init__(self, v):
        self.v = v
        self.r = None
        self.d = None

def loop(node, n):
    for _ in range(n):
        yield node
        node = node.r

def play(s, n, moves):
    cups = list(map(int, list(s)))
    first = Node(cups[0])
    prev = first
    n2node = {cups[0]: first}
    for i in range(1, n):
        v = cups[i] if i < len(cups) else i+1
        current = Node(v)
        prev.r = current
        n2node[v] = current
        prev = current
    for node in n2node.values():
        node.d = n2node[node.v - 1 if node.v > 1 else n]
    prev.r = first
    current = first
    for i in range(moves):
        x, y, z = current.r, current.r.r, current.r.r.r
        dest = current.d
        while dest.v in (x.v, y.v, z.v):
            dest = dest.d
        # remove x, y, z
        current.r = z.r
        # move them after d
        old_dr = dest.r
        dest.r = x
        z.r = old_dr
        current = current.r
    one = n2node[1]
    if n < 100:
        return ''.join(str(x.v) for x in loop(one.r, n-1))
    else:
        return one.r.v * one.r.r.v

for s in ('389125467', '398254716'):
    print('*** %s' % s)
    print(play(s, len(s), 100))
    print(play(s, 1000000, 10000000))