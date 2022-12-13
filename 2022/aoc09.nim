import strutils, tables, math, sets, algorithm
type
    Point = object
        x, y: int
proc `-`(a, b: Point): Point = Point(x: a.x - b.x, y: a.y - b.y)
proc `+`(a, b: Point): Point = Point(x: a.x + b.x, y: a.y + b.y)

let offsets = {
    "U": Point(x: 0, y: 1),
    "R": Point(x: 1, y: 0),
    "D": Point(x: 0, y: -1),
    "L": Point(x: -1, y: 0),
}.toTable

var snake: array[10, Point]
snake.fill(Point(x: 0, y: 0))
var visited = initHashSet[Point]()
var visited9 = initHashSet[Point]()

for line in "09.txt".lines:
    let parts = line.split()
    for _ in 1..parts[1].parseInt:
        let dir = parts[0]
        snake[0] = snake[0] + offsets[dir]
        for i in 1..9:
            let diff = snake[i-1] - snake[i]
            if diff.x.abs > 1 or diff.y.abs > 1:
                snake[i] = snake[i] + Point(x: diff.x.sgn, y: diff.y.sgn)
        visited.incl snake[1]
        visited9.incl snake[9]

echo "1⭐: ", visited.len
echo "2⭐: ", visited9.len
