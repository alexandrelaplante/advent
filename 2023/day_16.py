UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"


data = []
test_data = []

with open("/home/alex/advent_of_code/day_16.txt", "r") as f:
    for line in f:
        data.append(line)


with open("/home/alex/advent_of_code/day_16_test.txt", "r") as f:
    for line in f:
        test_data.append(line)


def is_valid(rows: list[str], x: int, y: int):
    return 0 <= x < len(rows[0]) and 0 <= y < len(rows)


def next_beams(rows: list[str], x: int, y: int, direction: str):
    try:
        if direction == UP:
            c = rows[y - 1][x]
        if direction == LEFT:
            c = rows[y][x - 1]
        if direction == DOWN:
            c = rows[y + 1][x]
        if direction == RIGHT:
            c = rows[y][x + 1]
    except:
        return

    if direction == UP:
        if c in ".|":
            yield (x, y - 1, UP)
        if c == "\\":
            yield (x, y - 1, LEFT)
        if c == "/":
            yield (x, y - 1, RIGHT)
        if c == "-":
            yield (x, y - 1, LEFT)
            yield (x, y - 1, RIGHT)

    if direction == RIGHT:
        if c in ".-":
            yield (x + 1, y, RIGHT)
        if c == "\\":
            yield (x + 1, y, DOWN)
        if c == "/":
            yield (x + 1, y, UP)
        if c == "|":
            yield (x + 1, y, UP)
            yield (x + 1, y, DOWN)

    if direction == DOWN:
        if c in ".|":
            yield (x, y + 1, DOWN)
        if c == "\\":
            yield (x, y + 1, RIGHT)
        if c == "/":
            yield (x, y + 1, LEFT)
        if c == "-":
            yield (x, y + 1, LEFT)
            yield (x, y + 1, RIGHT)

    if direction == LEFT:
        if c in ".-":
            yield (x - 1, y, LEFT)
        if c == "\\":
            yield (x - 1, y, UP)
        if c == "/":
            yield (x - 1, y, DOWN)
        if c == "|":
            yield (x - 1, y, UP)
            yield (x - 1, y, DOWN)


def find_energy(rows: list[str], start_x: int, start_y: int, start_dir: str) -> int:
    visited = set()
    visited_directional = set()

    to_visit = [(start_x, start_y, start_dir)]
    while len(to_visit) > 0:
        x, y, dir = to_visit.pop(0)

        visited.add((x, y))
        visited_directional.add((x, y, dir))

        valid_next = [
            b
            for b in next_beams(rows, x, y, dir)
            if is_valid(rows, b[0], b[1]) and not b in visited_directional
        ]
        to_visit.extend(valid_next)

    # print(visited)

    # for y, row in enumerate(rows):
    #     out = []
    #     for x, c in enumerate(row):
    #         if (x, y) in visited:
    #             out.append("#")
    #         else:
    #             out.append(".")
    #     print("".join(out))

    return len(visited) - 1


def part1(data):
    rows = data

    return find_energy(rows, -1, 0, RIGHT)


def part2(data):
    rows = data

    best = 0
    for x in range(len(rows[0])):
        for y in range(len(rows)):
            if y == 0:
                best = max(best, find_energy(rows, x, y - 1, DOWN))
            if y == len(rows) - 1:
                best = max(best, find_energy(rows, x, y + 1, UP))
            if x == 0:
                best = max(best, find_energy(rows, x - 1, y, RIGHT))
            if x == len(rows[0]) - 1:
                best = max(best, find_energy(rows, x + 1, y, LEFT))

    return best


print(part1(data))
print(part2(data))
