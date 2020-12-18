import re

def evaluate(s, prio):
    i, values, ops = 0, [], []
    while i < len(s):
        if s[i] == ' ':
            i = i + 1
            continue
        elif s[i] == '(':
            ops.append(s[i])
        elif s[i].isdigit():
            n = re.match(r'^(\d+)', s[i:])[1]
            i = i + len(n) - 1
            values.append(int(n))
        elif s[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                values.append(eval('%d%s%d' % (values.pop(), ops.pop(), values.pop())))
            ops.pop() # (
        else:
            while len(ops) != 0 and prio[ops[-1]] >= prio[s[i]]:
                values.append(eval('%d%s%d' % (values.pop(), ops.pop(), values.pop())))
            ops.append(s[i])
        i = i + 1
    while len(ops) != 0:
        values.append(eval('%d%s%d' % (values.pop(), ops.pop(), values.pop())))
    return values[-1]


for f in ('sample18.txt', 'input18.txt'):
    print('\n***', f)
    lines = [line.strip() for line in open(f).readlines()]
    prio = {'+': 1, '-': 1, '*': 1, '(': 0, ')': 0}
    print(sum(evaluate(line, prio) for line in lines))
    prio = {'+': 2, '-': 2, '*': 1, '(': 0, ')': 0}
    print(sum(evaluate(line, prio) for line in lines))