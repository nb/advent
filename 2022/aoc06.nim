import sugar, sets, sequtils

let input = readFile("06.txt")
proc solve(s: string, n: int): int =
    (0..len(s)-n).toSeq.filter(i => s[i..i+n-1].toHashSet.len == n)[0] + n
echo "1⭐: ", solve(input, 4)
echo "2⭐: ", solve(input, 14)