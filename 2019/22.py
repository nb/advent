def part1(lines, n):
    deck = list(range(n))
    for line in lines:
        parts = line.strip().split(' ')
        if line.startswith('deal with'):
            increment = int(parts[-1])
            i = 0
            newdeck = [None] * len(deck)
            for _ in range(n):
                newdeck[i] = deck.pop(0)
                i = (i + increment) % n
            deck = newdeck
        if line.startswith('deal into new'):
            deck.reverse()
        if line.startswith('cut'):
            cut = int(parts[-1])
            deck = deck[cut:] + deck[:cut]
    if n < 2019:
        return deck
    else:
        return deck.index(2019)

"""
here are the ways the position (0-based) of a number changes, based on the technique:
new: nextpos(i) = n - i - 1, same as (-i-1) mod n (at least in python)
inc: nextpos(i) = (k * i) mod n – increment is k
cut: nextpos(i) = (i - k) mod n – we cut by k – works for negatives, too (at least in python)

example:
n = 10
9876543210
new ⇒ the new position of the number 6 should be -4 % 10 = 6, which in 0123456789 is true!
0123456789
inc 3 ⇒ the new position of the number 6 should be (3*6)%10 = 8, which in 0741852963 is true!
cut 3 ⇒ the new position of the number 6 should be (6-3)%10 = 3, which in 3456789012 is true!
cut -4 ⇒ the new position of the number 6 should be (6+4)%10 = 0, which in 6789012345 is true!

applying all techniques will give us a formula for each index in constant memory and O(# of techniques)
since all nextpos(i) options look like a*i+b, applying them one after at the end will give us a formula
that also looks like a*i+b and we will just calculate the a and b for applying all the techniques in
our list
"""
def part2(lines):
    n = 119315717514047
    a, b = 1, 0
    for line in lines:
        parts = line.strip().split(' ')
        """
        inext = nextpos(i) = ta*i + tb (ta and tb depend on the technique)
        i = a*i + b
        inext = ta*(a*i+b) + tb = (ta*a)*i + (ta*b + tb)
        ⇒ newa = ta*a, newb = ta*b + tb
        """
        if line.startswith('deal with'):
            increment = int(parts[-1])
            ta, tb = increment, 0
        if line.startswith('deal into new'):
            ta, tb = -1, -1
        if line.startswith('cut'):
            cut = int(parts[-1])
            ta, tb = 1, -cut
        a, b = (a*ta) % n, (ta*b + tb) % n
    """
    now, we need to apply the same thing M times
    for a, it's easy – it's just a^M % n
    """
    M = 101741582076661
    ma = pow(a, M, n)
    """
    for b it's a bit more complicated
    b[m] = b*(1+a+a^2+a^3…+a^(m-1))
    it's a common formula that 1+a+a^2+a^3…+a^(m-1) = (a^m - 1)/(a-1)
    tip: to prove, first multiply by x, then add 1 to each side
    luckily, python supports modinv via supplying -1 as the power (since 3.8)
    """
    mb = (b * (ma - 1) * pow(a-1, -1, n)) % n
    """
    final frontier: we don't need the final position of 2020, but we need the card on position 2020
    final position of card i is (ma*i + mb) % n and we need to find i, where:
    ma*i + mb % n = 2020
    ma*i % n = 2020-mb
    ⇒ i % n = (2020-mb)%n * (1/ma)*n = (2020-mb)%n * modinv(ma, n)
    """
    v = 2020
    return ((v - mb) * pow(ma, -1, n)) % n

for f in ('sample22.txt', 'input22.txt'):
    print('\n***', f)
    lines = open(f).readlines()
    print(part1(lines, 10 if f.startswith('sample') else 10007))
    if not f.startswith('sample'):
        print(part2(lines))
