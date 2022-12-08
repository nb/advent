import std/[re, tables, strutils, sequtils, sugar]

var stacks = initTable[int, seq[char]]()
var superstacks = initTable[int, seq[char]]()

for line in "05.txt".lines:
    if line == "":
        # copy for 2nd star
        superstacks = stacks
        continue
    # in reality those may not be the 1-X numbers, but artibtary ones
    if line.startsWith(" 1"):
        continue
    if line.startsWith("move"):
        var matches: array[3, string]
        if match(line, re"move (\d+) from (\d+) to (\d+)", matches):
            let command = matches.map(parseInt)
            # 1st star
            for _ in 1..command[0]:
                stacks[command[2]-1].add(stacks[command[1]-1].pop())
            # 2nd star
            superstacks[command[2]-1].add(superstacks[command[1]-1][^command[0]..^1])
            # superstacks[command[1]-1].delete(^command[0]..^1) didn't work
            superstacks[command[1]-1].delete(len(superstacks[command[1]-1])-command[0]..len(superstacks[command[1]-1])-1)
        continue
    for i, token in pairs(re.findAll(line, re"\[\w\]| .  ")):
        if token.startsWith("["):
            if not (i in stacks):
                stacks[i] = @[]
            stacks[i] = token[1] & stacks[i]

echo "1⭐: ", (0..(len(stacks)-1)).toSeq.map(i => stacks[i][^1]).join("")
echo "2⭐: ", (0..(len(superstacks)-1)).toSeq.map(i => superstacks[i][^1]).join("")