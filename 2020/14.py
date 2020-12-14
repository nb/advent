from itertools import chain, combinations
import re


def subsets(s):
    return map(set, chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


def ops(lines):
    for line in lines:
        if line.startswith('mask = '):
            mask = line[7:]
            yield 'mask', mask
        else:
            addr, n = map(int, re.match(
                r'mem\[(\d+)\] = (\d+)', line).group(1, 2))
            yield 'assign', (addr, n, bin(n)[2:].zfill(36), bin(addr)[2:].zfill(36))


for f in ('sample14.txt', 'sample14-2.txt', 'input14.txt'):
    print('\n***', f)
    lines = [line.strip() for line in open(f).readlines()]

    mask = None
    mem = {}
    for op in ops(lines):
        command, args = op
        if command == 'mask':
            mask = args
            continue
        addr, n, nbin, _ = args
        masked = [m if m != 'X' else b for b, m in zip(nbin, mask)]
        mem[addr] = int(''.join(masked), 2)
    print(sum(mem.values()))

    if (f == 'sample14.txt'):
        # too many Xs
        continue

    mask = None
    mem = {}
    for op in ops(lines):
        command, args = op
        if command == 'mask':
            mask = args
            continue
        _, n, _, addrbin = args
        masked = [b if m == '0' else m for b, m in zip(addrbin, mask)]
        X_indices = set(i for i, bit in enumerate(masked) if bit == 'X')
        for subset in subsets(X_indices):
            for i in subset:
                masked[i] = '1'
            for i in X_indices - subset:
                masked[i] = '0'
            mem[int(''.join(masked), 2)] = n
    print(sum(mem.values()))
