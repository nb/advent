import sys
from itertools import combinations
sys.setrecursionlimit(10000)
for f in ('sample9.txt', 'input9.txt'):
    print(f)
    numbers = [int(line.strip()) for line in open(f).readlines()]
    first = None
    offset = 25 if f != 'sample9.txt' else 5
    first = next(n for i, n in enumerate(numbers[offset:], start=offset) if not any(
        n == a+b for a, b in combinations(numbers[i-offset:i], r=2)))
    print(first)

    def find(total, start=0, end=0):
        if total == first:
            return start, end
        if total < first:
            return find(total + numbers[end+1], start, end + 1)
        else:
            return find(total - numbers[start], start + 1, end)
    start, end = find(numbers[0])
    result_range = numbers[start:end+1]
    print(min(result_range) + max(result_range))
    print()
