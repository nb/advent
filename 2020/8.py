def replaced(ops):
    for i, op in enumerate(ops):
        if op['op'] == 'nop':
            yield i, 'jmp'
        if op['op'] == 'jmp':
            yield i, 'nop'


def execute(ops, index=None, override=None):
    acc = 0
    i = 0
    visited = set()
    while i < len(ops):
        op = ops[i] if i != index else {'op': override, 'num': ops[i]['num']}
        if i in visited:
            return (acc, False)
        visited.add(i)
        if op['op'] == 'acc':
            acc = acc + op['num']
        if op['op'] == 'jmp':
            i = i + op['num']
        else:
            i = i + 1
    return (acc, True)


for f in ('sample8.txt', 'input8.txt'):
    ops = [{'op': line.split()[0], 'num': int(line.split()[1])}
           for line in open(f).readlines()]
    print(f)
    print(execute(ops))
    for i, override in replaced(ops):
        (acc, success) = execute(ops, i, override)
        if success:
            print(acc)
            break
