import itertools
from typing import Iterator

INPUT = """Register A: 63687530
Register B: 0
Register C: 0

Program: 2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0"""

TEST = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

TEST2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


"""
Program analysis:

(2, 4):    b <- a % 8
(1, 3):    b <- b ^ 3
(7, 5):    c <- a // (2 ** b)
(0, 3):    a <- a // (2 ** 3)
(1, 5):    b <- b ^ 5
(4, 1):    b <- b ^ c
(5, 5):    yield (b % 8)
(3, 0):    (a != 0) -> jmp 0

Rewritten:

while a != 0:
    b = a % 8
    b = b ^ 3
    c = a // (2 ** b)
    a = a // (2 ** 3)
    b = b ^ 5 ^ c
    yield b % 8

Shorter:

while a != 0:
    b = (a % 8) ^ 3
    c = a // (2**b)
    a = a // 8
    yield (b ^ 5 ^ c) % 8

while a != 0:
    b = (last 3 bits of a) ^ 3
    c = truncate last b bits of a
    a = truncate last 3 bits of a
    yield (b ^ 5 ^ c) % 8

Do % and ^ commute? if so we could figure out all the bits of a separately.
Yes they do!
(b ^ 5 ^ c) % 8 == (b%8) ^ 5 ^ (c%8)

while a != 0:
    b = (last 3 bits of a) ^ 3  # 0 <= b <= 8
    c = truncate last b bits of a
    a = truncate last 3 bits of a
    yield (last 3 bits of b) ^ 5 ^ (last 3 bits of c)

bbbbbbbbbbbbbbbbbbbbb
          XXX     XXX

The first digit can only be impacted by the last 11 bits of a.
The nth digit (starting at 0) can only be impacted by the (len-11-n, len-n)) bits of a.


If we fix the earlier digits first, then the nth bit is only a function of 3 bits (len-n-3, len-n) of a
"""


def compute(a, b, c, program) -> Iterator[int]:
    def combo(n: int) -> int:
        if 0 <= n <= 3:
            return n
        elif n == 4:
            return a
        elif n == 5:
            return b
        elif n == 6:
            return c
        else:
            raise

    ip = 0

    while ip < len(program) - 1:
        opcode, operand = program[ip], program[ip + 1]
        if opcode == 0:  # adv
            a = a // (2 ** combo(operand))
        elif opcode == 1:  # bxl
            b = b ^ operand
        elif opcode == 2:  # bst
            b = combo(operand) % 8
        elif opcode == 3:  # jnz
            if a != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            b = b ^ c
        elif opcode == 5:  # out
            yield combo(operand) % 8
        elif opcode == 6:  # bdv
            b = a // (2 ** combo(operand))
        elif opcode == 7:  # cdv
            c = a // (2 ** combo(operand))

        ip += 2


def part1(INPUT):
    registers, program = INPUT.split("\n\n")
    registers = registers.split("\n")
    a = int(registers[0].split(": ")[1])
    b = int(registers[1].split(": ")[1])
    c = int(registers[2].split(": ")[1])
    program = [int(d) for d in program[9:].split(",")]

    print(a, b, c, program)

    out = list(compute(a, b, c, program))

    print(",".join(map(str, out)))


def compute2(a: int) -> Iterator[int]:
    while a != 0:
        b = (a % 8) ^ 3
        c = a // (2**b)
        a = a // 8
        yield (b ^ 5 ^ c) % 8


PROGRAM = [2, 4, 1, 3, 7, 5, 0, 3, 1, 5, 4, 1, 5, 5, 3, 0]


def backtrack(a, i) -> int | None:
    print(a, i)
    if i == -1:
        return a
    for bits in range(8):
        new_a = a + (bits << (i * 3))
        computed = list(compute2(new_a))
        # if it's a partial solution, recurse
        try:
            if computed[i] == PROGRAM[i]:
                result = backtrack(new_a, i - 1)
                if result is not None:
                    return result
        except IndexError:
            pass
    return None


def part2_backtrack():
    result = backtrack(0, len(PROGRAM) - 1)
    print(result)

part1(INPUT)
part2_backtrack()
