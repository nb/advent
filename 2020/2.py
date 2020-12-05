def rulefromparts(parts):
    numbers = parts[0].split('-')
    return {'letter': parts[1][0], 'first': int(numbers[0]), 'second': int(numbers[1]), 'password': parts[2]}


def min_max(rule):
    occurrences = rule['password'].count(rule['letter'])
    return occurrences >= rule['first'] and occurrences <= rule['second']


def pos(rule):
    return (rule['password'][rule['first']-1] == rule['letter']) != (rule['password'][rule['second']-1] == rule['letter'])


def count_valid(is_valid_function):
    return sum(is_valid_function(rulefromparts(line.strip().split(
        ' '))) for line in open('input2.txt').readlines())


print(count_valid(min_max))
print(count_valid(pos))
