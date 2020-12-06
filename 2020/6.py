from string import ascii_lowercase
from functools import reduce
for f in ('sample6.txt', 'input6.txt'):
    groups = open(f).read().split('\n\n')
    print(sum([len(set(group.replace('\n', '')))
               for group in groups]))
    print(sum(map(len, [reduce(lambda x, y: x & set(y), group.split(
        '\n'), set(ascii_lowercase)) for group in groups])))
