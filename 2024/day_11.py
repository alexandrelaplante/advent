INPUT = """510613 358 84 40702 4373582 2 0 1584"""

TEST = """125 17"""


def part1(INPUT):
    old_list = [int(n) for n in INPUT.split(" ")]

    for _ in range(25):
        new_list = []
        for n in old_list:
            if n == 0:
                new_list.append(1)
            elif (digits := len(str(n))) % 2 == 0:
                new_list.append(int(str(n)[: digits // 2]))
                new_list.append(int(str(n)[digits // 2 :]))
            else:
                new_list.append(2024 * n)
        old_list = new_list

    print(len(old_list))


class Blinker:
    def __init__(self) -> None:
        self.cache = {}

    def blink(self, n: int, times: int) -> int:
        """returns the number of stones after blinking times times"""
        if times == 0:
            return 1

        if (n, times) in self.cache:
            return self.cache[(n, times)]

        if n == 0:
            stones = self.blink(1, times=times - 1)
        elif (digits := len(str(n))) % 2 == 0:
            left = int(str(n)[: digits // 2])
            right = int(str(n)[digits // 2 :])
            stones = self.blink(left, times=times - 1) + self.blink(
                right, times=times - 1
            )
        else:
            stones = self.blink(2024 * n, times=times - 1)

        self.cache[(n, times)] = stones
        return stones


def part2(INPUT):
    old_list = [int(n) for n in INPUT.split(" ")]

    blinker = Blinker()
    total = sum(blinker.blink(n, 75) for n in old_list)

    print(total)


part1(INPUT)
part2(INPUT)
