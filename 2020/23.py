class Node():
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

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
        current = Node(v, prev)
        prev.r = current
        n2node[v] = current
        prev = current
    first.l = prev
    prev.r = first
    current = first
    for i in range(moves):
        if moves > 1000 and i % 1000000 == 0:
            print('\tprogress %d' % i)
        x, y, z = current.r, current.r.r, current.r.r.r
        d = current.v - 1
        while True:
            if d in (x.v, y.v, z.v) or d < 1 or d > n:
                d = d - 1 if d >= 1 else n
            else:
                break
        dnode = n2node[d]
        # remove x, y, z
        current.r = z.r
        z.r.l = current
        # move them after d
        old_dr = dnode.r
        dnode.r = x
        old_dr.l = z
        z.r = old_dr
        x.l = dnode
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