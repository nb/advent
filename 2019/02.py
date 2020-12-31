from operator import add, mul

def run(program):
    ip = 0
    while True:
        if program[ip] == 99:
            break
        op = add if program[ip] == 1 else mul
        program[program[ip+3]] = op(program[program[ip+1]], program[program[ip+2]])
        ip += 4
    return program

for f in ('sample02.txt', 'input02.txt'):
    print('\n***', f)
    original_program = list(map(int, [line.strip() for line in open(f).readlines()][0].split(',')))
    program = original_program[:]
    if f.startswith('input'):
        program[1] = 12
        program[2] = 2
    print(run(program)[0])
    for a in range(min(100, len(original_program))):
        for b in range(min(100, len(original_program))):
            program = original_program[:]
            program[1] = a
            program[2] = b
            if run(program)[0] == 19690720:
                print(a*100+b)
