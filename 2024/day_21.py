from __future__ import annotations

from typing import Iterator

KEYPAD = """789
456
123
.0A"""

DIRPAD = """.^A
<v>"""

INPUT = """480A
143A
983A
382A
974A"""

TEST = """029A
980A
179A
456A
379A"""


from dataclasses import dataclass


@dataclass
class Vec2:
    x: int
    y: int

    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)

    def copy(self) -> "Vec2":
        return Vec2(self.x, self.y)


def flatten(xss):
    return [x for xs in xss for x in xs]


def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result


def code_permutations(code: list[str]) -> Iterator[list[str]]:
    import itertools

    split = "".join(code).split("A")
    possibilities = []
    for symbols in split:
        possibilities.append(set(itertools.permutations(symbols)))
    for possibility in itertools.product(*possibilities):
        yield flatten(intersperse(possibility, "A"))


def part1(INPUT):
    key_map: dict[str, Vec2] = {}
    dir_map: dict[str, Vec2] = {}

    for y, row in enumerate(KEYPAD.split("\n")):
        for x, c in enumerate(row):
            key_map[c] = Vec2(x, y)
    for y, row in enumerate(DIRPAD.split("\n")):
        for x, c in enumerate(row):
            dir_map[c] = Vec2(x, y)

    total = 0
    for output_code in INPUT.split("\n"):
        dir_code_1_guess: list[str] = []
        key_pos = key_map["A"]
        for symbol in output_code:
            sym_pos = key_map[symbol]
            # prefer going ^> over <v to avoid the gap
            to_move = sym_pos - key_pos
            while to_move != Vec2(0, 0):
                if to_move.y < 0:
                    dir_code_1_guess.append("^")
                    to_move.y += 1
                elif to_move.x > 0:
                    dir_code_1_guess.append(">")
                    to_move.x -= 1
                elif to_move.y > 0:
                    dir_code_1_guess.append("v")
                    to_move.y -= 1
                elif to_move.x < 0:
                    dir_code_1_guess.append("<")
                    to_move.x += 1
            dir_code_1_guess.append("A")
            key_pos = sym_pos

        def has_panic(code: list[str]) -> bool:
            key_pos = key_map["A"].copy()
            for symbol in code:
                if symbol == "^":
                    key_pos.y -= 1
                elif symbol == "v":
                    key_pos.y += 1
                elif symbol == "<":
                    key_pos.x -= 1
                elif symbol == ">":
                    key_pos.x += 1
                if key_pos == key_map["."]:
                    return True
            return False

        # try every permutation of the directions between As
        # print(dir_code_1)
        best1: list[str] | None = None
        best2: list[str] | None = None
        best3: list[str] | None = None
        for dir_code_1 in code_permutations(dir_code_1_guess):
            # print(dir_code_1)
            if has_panic(dir_code_1):
                # print("has_panic", dir_code_1)
                continue

            dir_code_2: list[str] = []
            dir_pos = dir_map["A"]
            for symbol in dir_code_1:
                sym_pos = dir_map[symbol]
                # prefer going v> over <^ to avoid the gap
                to_move = sym_pos - dir_pos
                while to_move != Vec2(0, 0):
                    if to_move.y > 0:
                        dir_code_2.append("v")
                        to_move.y -= 1
                    elif to_move.x > 0:
                        dir_code_2.append(">")
                        to_move.x -= 1
                    elif to_move.y < 0:
                        dir_code_2.append("^")
                        to_move.y += 1
                    elif to_move.x < 0:
                        dir_code_2.append("<")
                        to_move.x += 1
                dir_code_2.append("A")
                dir_pos = sym_pos

            dir_code_3: list[str] = []
            dir_pos = dir_map["A"]
            for symbol in dir_code_2:
                sym_pos = dir_map[symbol]
                # prefer going v> over <^ to avoid the gap
                to_move = sym_pos - dir_pos
                while to_move != Vec2(0, 0):
                    if to_move.y > 0:
                        dir_code_3.append("v")
                        to_move.y -= 1
                    elif to_move.x > 0:
                        dir_code_3.append(">")
                        to_move.x -= 1
                    elif to_move.y < 0:
                        dir_code_3.append("^")
                        to_move.y += 1
                    elif to_move.x < 0:
                        dir_code_3.append("<")
                        to_move.x += 1
                dir_code_3.append("A")
                dir_pos = sym_pos

            if (not best3) or len(dir_code_3) < len(best3):
                best1 = dir_code_1
                best2 = dir_code_2
                best3 = dir_code_3

        if best1 and best2 and best3:
            mult = int("".join(d for d in output_code if d in "0123456789"))
            print(output_code, ":", "".join(best1))
            print(output_code, ":", "".join(best2))
            print(output_code, ":", "".join(best3))
            print(len(best3), "*", mult)
            print()

            total += len(best3) * mult

    print(total)


from functools import cache


def part2(INPUT: str, depth: int):
    key_map: dict[str, Vec2] = {}
    dir_map: dict[str, Vec2] = {}

    for y, row in enumerate(KEYPAD.split("\n")):
        for x, c in enumerate(row):
            key_map[c] = Vec2(x, y)
    for y, row in enumerate(DIRPAD.split("\n")):
        for x, c in enumerate(row):
            dir_map[c] = Vec2(x, y)

    total = 0
    for output_code in INPUT.split("\n"):
        dir_code_1_guess: list[str] = []
        key_pos = key_map["A"]
        for symbol in output_code:
            sym_pos = key_map[symbol]
            to_move = sym_pos - key_pos
            while to_move != Vec2(0, 0):
                if to_move.y < 0:
                    dir_code_1_guess.append("^")
                    to_move.y += 1
                elif to_move.x > 0:
                    dir_code_1_guess.append(">")
                    to_move.x -= 1
                elif to_move.y > 0:
                    dir_code_1_guess.append("v")
                    to_move.y -= 1
                elif to_move.x < 0:
                    dir_code_1_guess.append("<")
                    to_move.x += 1
            dir_code_1_guess.append("A")
            key_pos = sym_pos

        def has_panic(code: list[str]) -> bool:
            key_pos = key_map["A"].copy()
            for symbol in code:
                if symbol == "^":
                    key_pos.y -= 1
                elif symbol == "v":
                    key_pos.y += 1
                elif symbol == "<":
                    key_pos.x -= 1
                elif symbol == ">":
                    key_pos.x += 1
                if key_pos == key_map["."]:
                    return True
            return False

        def get_possible_parent_input(from_symbol: str, to_symbol: str) -> list[str]:
            symbols = "".join([from_symbol, to_symbol])
            mapping = {
                "AA": ["A"],
                "A^": ["<A"],
                "A>": ["vA"],
                "Av": ["v<A", "<vA"],
                "A<": ["v<<A", "<v<A"],
                "^A": [">A"],
                "^^": ["A"],
                "^>": ["v>A", ">vA"],
                "^v": ["vA"],
                "^<": ["v<A"],
                ">A": ["^A"],
                ">^": ["^<A", "<^A"],
                ">>": ["A"],
                ">v": ["<A"],
                "><": ["<<A"],
                "vA": [">^A", "^>A"],
                "v^": ["^A"],
                "v>": [">A"],
                "vv": ["A"],
                "v<": ["<A"],
                "<A": [">>^A", ">^>A"],
                "<^": [">^A"],
                "<>": [">>A"],
                "<v": [">A"],
                "<<": ["A"],
            }
            return mapping[symbols]

        @cache
        def get_count(from_symbol: str, to_symbol: str, depth: int) -> int:
            best: int | None = None
            for parent_input in get_possible_parent_input(from_symbol, to_symbol):
                if depth == 1:
                    return len(parent_input)

                total = 0
                last_symbol = "A"
                for symbol in parent_input:
                    total += get_count(last_symbol, symbol, depth - 1)
                    last_symbol = symbol
                if (not best) or total < best:
                    best = total
            return best

        # try every permutation of the directions between As
        best: int | None = None
        for dir_code_1 in code_permutations(dir_code_1_guess):
            if has_panic(dir_code_1):
                continue

            count = 0
            last_symbol = "A"
            for symbol in dir_code_1:
                count += get_count(last_symbol, symbol, depth)
                last_symbol = symbol

            if (not best) or count < best:
                best = count

        if best:
            mult = int("".join(d for d in output_code if d in "0123456789"))
            print(best, "*", mult)

            total += best * mult

    print(total)
    print()


# part1(INPUT)
part2(INPUT, depth=2)
part2(INPUT, depth=25)
