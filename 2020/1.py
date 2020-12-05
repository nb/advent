numbers = set(map(int, open('input1.txt').readlines()))
for n in numbers:
    if (2020-n) in numbers:
        print(n, n*(2020-n))

for a in numbers:
    for b in numbers:
        if (2020-a-b) in numbers:
            print(a, b, a*b*(2020-a-b))
