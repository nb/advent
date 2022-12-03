import std/[sequtils, tables]
import math
let n = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}.toTable
let w = {"A Y": 6, "B X": 0, "A Z": 0, "C X": 6, "B Z": 6, "C Y": 0}.toTable
echo "1⭐: ", "02.txt".lines.toSeq.mapIt(n[it[2]] + (if n[it[0]] == n[it[2]]: 3 else: w[it])).sum
echo "1⭐: ", "02.txt".lines.toSeq.mapIt(n[it[2]] + ((n[it[2]] - n[it[0]] + 1 + 6) mod 3) * 3).sum
echo "2⭐: ", "02.txt".lines.toSeq.mapIt((n[it[2]] - 1) * 3 + (n[it[0]] + n[it[2]]) mod 3 + 1).sum