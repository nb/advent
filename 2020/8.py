for f in ('sample8.txt', 'input8.txt'):
    lines = list(open(f).readlines())
    acc = 0
    i = 0
    visited = set()
    while i < len(lines):
        line = lines[i]
        if i in visited:
            print(acc)
            break
        visited.add(i)
        op, num = line.strip().split()
        num = int(num)
        print(op, num, acc)
        if op == 'acc':
            acc = acc + num
        if op == 'jmp':
            i = i + num
        else:
            i = i + 1
