def set_orbits(object, distance = 0):
    orbits[object] = distance
    for child in filter(lambda child: parents[child] == object, parents):
        set_orbits(child, distance + 1)

for f in ('sample06.txt', 'input06.txt'):
    print('\n***', f)
    lines = [line.strip() for line in open(f).readlines()]
    parents = {line.split(')')[1]: line.split(')')[0] for line in lines}
    orbits = {}
    set_orbits('COM')
    print(sum(orbits.values()))
    if not 'SAN' in parents:
        continue
    # find least common ancestor for SAN and YOu
    path_SAN = set()
    lca = 'SAN'
    while lca != 'COM':
        path_SAN.add(parents[lca])
        lca = parents[lca]
    lca = 'YOU'
    while not lca in path_SAN:
        lca = parents[lca]
    print(orbits['SAN'] + orbits['YOU'] - 2 - 2*orbits[lca])