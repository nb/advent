import sets, tables, strutils, sequtils, math
var cd = ""
var directories = ["/"].toHashSet
var files = initTable[string, int]()

proc up(s: string): string =
    return s[0 .. s[0 .. ^2].rfind("/")]

proc size(dir: string): int =
    var total = 0
    for file, size in files:
        if file.startsWith(dir):
            total += size
    return total

for line in "07.txt".lines.toSeq:
    let parts = line.split()
    if parts[0] != "$" and parts[0] != "dir":
        files[cd & parts[1]] = parts[0].parseInt
        continue
    if parts[1] == "cd" and parts[2] == "/":
        cd = "/"
        continue
    if parts[1] == "cd" and parts[2] == "..":
        cd = up(cd)
        directories.incl(cd)
        continue
    if parts[1] == "cd" and parts[2] != "..":
        cd = cd & parts[2] & "/"
        directories.incl(cd)
        continue

let root = size("/")
echo "1⭐: ", directories.toSeq.map(size).filterIt(it <= 100_000).sum
echo "2⭐: ", directories.toSeq.filterIt(70_000_000 - root + size(it) > 30_000_000).map(size).min