import std/[strutils, sequtils]
import math
type 
    Ranges = object
        a: int
        b: int
        c: int
        d: int
proc parse(line: string): Ranges = 
  let pairs = line.split(",")

  return Ranges(a: pairs[0].split('-')[0].parseInt,
                    b: pairs[0].split('-')[1].parseInt,
                    c: pairs[1].split('-')[0].parseInt,
                    d: pairs[1].split('-')[1].parseInt)

proc contains(r: Ranges): bool =
    return (r.a >= r.c and r.b <= r.d) or (r.c >= r.a and r.d <= r.b)

proc overlaps(r: Ranges): bool =
    # we need the +1 to account for numbers at the end of the range
    # being included in the range
    return max(0, min(r.b, r.d) - max(r.a, r.c) + 1) > 0

echo "1⭐: ", "04.txt".lines.toSeq.mapIt(int(contains(parse(it)))).sum
echo "2⭐: ", "04.txt".lines.toSeq.mapIt(int(overlaps(parse(it)))).sum