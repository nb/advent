for cpuk, dpuk in ((5764801, 17807724), (12232269, 19452773)):
    print('***', cpuk, dpuk)
    dloop, v = 0, 1
    while v != dpuk:
        dloop += 1
        v = (v * 7) % 20201227
    v = 1
    for _ in range(dloop):
        v = (v * cpuk) % 20201227
    print(v)