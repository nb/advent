from operator import add, mul
from collections import defaultdict

def run(program, input):
    ip = 0
    output = []
    immediate = set()
    arg = lambda i: program[ip+i+1] if i in immediate else program[program[ip+i+1]]
    while True:
        arity = 0
        jump = None
        opcode = program[ip]
        immediate = set()
        if program[ip] > 100:
            opcode = program[ip] % 100
            immediate = {i for i, x in enumerate(map(int, (reversed(list(str(program[ip] // 100)))))) if x == 1}
        if opcode == 99:
            break
        if opcode in (1, 2, 7, 8):
            arity = 3
            op = {
                1: add,
                2: mul,
                7: lambda a, b: int(a < b),
                8: lambda a, b: int(a == b),
            }[opcode]
            program[program[ip+3]] = op(arg(0), arg(1))
        if opcode == 3:
            arity = 1
            program[program[ip+1]] = input
        if opcode == 4:
            arity = 1
            output.append(program[program[ip+1]])
        if opcode in (5, 6):
            arity = 2
            go = (arg(0) != 0) if opcode == 5 else (arg(0) == 0)
            if go:
                jump = arg(1)
        if jump != None:
            ip = jump
        else:
            ip = ip + arity + 1
    return output

for f in ('sample05.txt', 'input05.txt'):
    print('\n***', f)
    original_program = list(map(int, (open(f).read().strip()).split(',')))
    print(run(original_program[:], 1))
    print(run(original_program[:], 5))