import sequtils, strutils, algorithm, math, sugar
let forest = lines("08.txt").toSeq.mapIt(it.toSeq.mapIt(($(it)).parseInt))
var visible = 0
var best = 0

# not super generic, might have been better to have written a specialized
# function to compute the view of a tree for each direction
iterator takeUntilInclusive*[T](a: openArray[T], f: proc(e: T): bool): T =
    for x in a:
        yield x
        if f(x):
            break

for i in 0 ..< forest.len:
  for j in 0 ..< forest[i].len:
    let paths = [
        forest[i][0..<j],
        forest[i][j+1..^1].reversed,
        forest[0..<i].mapIt(it[j]),
        forest[i+1..^1].mapIt(it[j]).reversed,
    ]
    # limitation of *It – nested its can be confusing
    if paths.anyIt(it.allIt(it < forest[i][j])):
      inc visible

    best = paths.mapIt(it.reversed.takeUntilInclusive(x => x >= forest[i][j]).toSeq.len).prod.max(best)

echo "1⭐: ", visible
echo "2⭐: ", best