from itertools import product, zip_longest

def split2(s, n):
    for i in range(len(s) // n - 1):
        split_len = (i+1)*n
        yield s[:split_len], s[split_len:]

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return (''.join(group) for group in zip_longest(*args))

def gen(rule_id):
    if rule_id in valid_for_rule_id:
        return valid_for_rule_id[rule_id]
    rule = rules[rule_id]
    result = set()
    if isinstance(rule, str):
        result = set(rule)
    else:
        for sub_rule_ids in rule:
            sets = (gen(sub_rule_id) for sub_rule_id in sub_rule_ids)
            result = result | {''.join(ordering) for ordering in product(*sets)}
    valid_for_rule_id[rule_id] = result
    return result

for f in ('sample19.txt', 'sample19-2.txt', 'input19.txt'):
    print('\n***', f)
    rules_part, messages_part = open(f).read().strip().split('\n\n')
    messages = messages_part.split('\n')

    rules, valid_for_rule_id = {}, {}

    for line in rules_part.split('\n'):
        n, rest = int(line.split(':')[0]), line.split(':')[1].strip()
        if '"' in rest:
            rules[n] = rest[1:-1]
        else:
            rules[n] = [list(map(int, r.strip().split(' '))) for r in rest.split('|')]

    gen(rule_id=0)

    print(sum(message in valid_for_rule_id[0] for message in messages))

    if not 8 in rules:
        continue

    N = len(next(iter(valid_for_rule_id[31])))
    rules[8] = [(42,), (42, 8)]
    rules[11] = [(42,31), (42, 11, 31)]

    is_repeat_of_rule = lambda message, rule_id: all(group in valid_for_rule_id[rule_id] for group in grouper(message, N))
    valid_for_rule_8 = lambda message: is_repeat_of_rule(message, 42)
    valid_for_rule_11 = lambda message: len(message) % (2*N) == 0 and is_repeat_of_rule(message[:len(message)//2], 42) and is_repeat_of_rule(message[len(message)//2:], 31)
    valid = lambda message: len(message) % N == 0 and any(valid_for_rule_8(left) and valid_for_rule_11(right) for left, right in split2(message, N))
    print(sum(valid(message) for message in messages))