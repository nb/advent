def seat_id(boarding_pass):
    row = int(boarding_pass[:7].replace('B', '1').replace('F', '0'), 2)
    column = int(boarding_pass[7:].replace('R', '1').replace('L', '0'), 2)
    id = row * 8 + column
    return id


for f in ('sample5.txt', 'input5.txt'):
    passes = map(str.strip, open(f).readlines())
    ids = sorted(map(seat_id, passes))
    print('max: ', ids[-1])
    for (id, next_id) in zip(ids, ids[1:]):
        print('my seat: ', id+1) if next_id != id+1 else None
