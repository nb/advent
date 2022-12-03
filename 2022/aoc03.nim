import std/[sets, sequtils]
import math


iterator chunks*[T](s: seq[T], size: int): seq[T] =
    var i = 0
    var chunk: seq[T] = @[]
    for x in s:
        if i >= size:
            yield chunk
            i = 0
            chunk = @[]
        inc i
        chunk.add x
    if len(chunk) > 0:
        yield chunk

proc prio(c: char): int =
    return if ord(c) < ord('a'):
        ord(c) - ord('A') + 1 + 26
    else:
        ord(c) - ord('a') + 1

# couldn't find a way to define this in a generic way
const h = (proc(keys: openArray[char]): HashSet[char])(toHashSet)

echo "1⭐: ", "03.txt".lines.toSeq.mapIt((h(it[0..len(it) div 2 - 1]) * h(it[len(it) div 2..^1])).items.toSeq[0].prio).sum
echo "2⭐: ", "03.txt".lines.toSeq.chunks(3).toSeq.mapIt((h(it[0]) * h(it[1]) * h(it[2])).items.toSeq[0].prio).sum