from functools import cache


def check_stone(num: int, check: int, count: list):
    if check == 25:
        count[0] += 1
        return

    if num == 0:
        check_stone(1, check + 1, count)
    elif len(str(num)) % 2 == 0:
        str_val = str(num)
        check_stone(int(str_val[int(len(str_val) / 2):]), check + 1, count)
        check_stone(int(str_val[:int(len(str_val) / 2)]), check + 1, count)
    else:
        check_stone(num * 2024, check + 1, count)


def part_1(content):
    counts = []
    for x in content:
        count = [0]
        check_stone(x, 0, count)
        counts += [count[0]]

    return sum(counts)


@cache
def check_stone_optimised(num: int, check: int, count: int):
    if check == 75:
        return count + 1

    if num == 0:
        return check_stone_optimised(1, check + 1, count)
    elif len(str(num)) % 2 == 0:
        str_val = str(num)
        return (check_stone_optimised(int(str_val[int(len(str_val) / 2):]), check + 1, count) +
                check_stone_optimised(int(str_val[:int(len(str_val) / 2)]), check + 1, count))

    else:
        return check_stone_optimised(num * 2024, check + 1, count)


def part_2(content):
    counts = []
    for x in content:
        count = check_stone_optimised(x, 0, 0)
        counts += [count]

    return sum(counts)


if __name__ == "__main__":
    file = open(r'data/day_11/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _content = [int(x) for x in _content[0].split(" ")]

    _count = part_1(_content)
    print(_count)

    _count = part_2(_content)
    print(_count)
    print("The size of the cached dictionary is:", check_stone_optimised.cache_info().currsize)
