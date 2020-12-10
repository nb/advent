from collections import Counter
for f in ('sample10.txt', 'input10.txt'):

    numbers = [int(line.strip()) for line in open(f).readlines()]
    numbers.sort()
    counts = Counter(b - a for a, b in zip([0] + numbers[:-1], numbers))
    print(counts[1] * (counts[3] + 1))

    cache = {}

    def ways(prev, i):
        if i == len(numbers) - 1:
            return 1
        if cache.get((prev, i)):
            return cache[(prev, i)]
        result = ways(numbers[i], i + 1)  # don't skip num i
        if numbers[i + 1] <= prev + 3:
            result = result + ways(prev, i + 1)  # skip num i
        cache[(prev, i)] = result
        return result
    print(ways(0, 0))
