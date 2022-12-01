import std/[strutils, sequtils, sugar, algorithm]
import math

# works!
# we need sugar for chaining and for => operator
let sums0 = (readFile("01.txt").split("\n\n")).map(elf => elf.split('\n').map(calorie => calorie.parseInt).sum)

# let's try collect, their version of multiline comprehensions
# I kinda like them better then yield
let elfs = (readFile("01.txt").split("\n\n"))
let sums = collect:
    for elf in elfs:
        let calories = collect:
            for calorie in elf.split('\n'):
                calorie.parseInt
        calories.sum

echo "max: ", sums.max
echo "sum of top 3: ", sums.sorted[^3..^1].sum

