file = open(r'data/day_1/part_1.txt', 'r')
_content = file.read().replace("\n", "-").split("-")
file.close()


def part_1(content: str):
    left = sorted([int(x.split(" ")[0]) for x in content])
    right = sorted([int(x.split(" ")[-1]) for x in content])

    dist = sum([abs(x - y) for x, y in zip(left, right)])

    return dist


print(f"part 1: {part_1(content=_content)}")


def part_2(content: str):
    left = [int(x.split(" ")[0]) for x in content]
    right = [int(x.split(" ")[-1]) for x in content]

    sim = 0
    for x in left:
        sim += x * right.count(x)

    return sim


print(f"part 2: {part_2(content=_content)}")

print()
