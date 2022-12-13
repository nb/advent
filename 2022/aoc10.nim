import strutils, sequtils
var next = 20
var X = 1
var oldX = 1
var current = 0
var strength = 0

var crt: array[6, array[40, bool]]

proc put() =
    if (X - (current mod 40)).abs <= 1:
        crt[current div 40][current mod 40] = true

for line in "10.txt".lines:
    let parts = line.split()
    put()
    if parts[0] == "noop":
        oldX = X
        inc current, 1
    else:
        inc current, 1
        put()
        inc current, 1
        oldX = X
        inc X, parts[1].parseInt
    if current >= next:
        if current == next and parts[0] == "noop":
            inc strength, X * next
        else:
            inc strength, oldX * next
        inc next, 40
echo "1⭐: ", strength
echo "2⭐: "
for row in crt:
  echo row.mapIt(if it: "#" else: " ").join