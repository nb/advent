import re


def is_valid(passport):
    fields = 'byr iyr eyr hgt hcl ecl pid'.split()
    return all(field in passport for field in fields)


def is_super_valid(passport):
    if not is_valid(passport):
        return False
    is_entry_valid = {
        'byr': lambda x: bool(re.match(r'^\d\d\d\d$', x)) and int(x) >= 1920 and int(x) <= 2002,
        'iyr': lambda x: bool(re.match(r'^\d\d\d\d$', x)) and int(x) >= 2010 and int(x) <= 2020,
        'eyr': lambda x: bool(re.match(r'^\d\d\d\d$', x)) and int(x) >= 2020 and int(x) <= 2030,
        'hgt': lambda x: (bool(re.match(r'^\d{2,3}(cm|in)$', x))) and ((int(x[:-2]) >= 150 and int(x[:-2]) <= 193) if x[-2:] == 'cm' else (int(x[:-2]) >= 59 and int(x[:-2]) <= 76)),
        'hcl': lambda x: bool(re.match(r'^#[0-9a-f]{6}$', x)),
        'ecl': lambda x: x in 'amb blu brn gry grn hzl oth'.split(),
        'pid': lambda x: bool(re.match(r'^[0-9]{9}$', x)),
        'cid': lambda x: True
    }
    entries = re.findall(r'(\S+):(\S+)', passport)
    return all(is_entry_valid[field](value) for field, value in entries)


for f in ('sample4.txt', 'input4.txt'):
    passports = open(f).read().split('\n\n')
    print(sum(is_valid(passport) for passport in passports))
    print(sum(is_super_valid(passport) for passport in passports))
