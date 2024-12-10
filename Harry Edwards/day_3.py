import re


def part_1(content):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    working = re.findall(pattern, content)
    total = sum(int(x[x.find('(') + 1:x.find(',')]) * int(x[x.find(',') + 1: x.find(')')]) for x in working)

    return total


def part_2(content):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    content = content.split("don't()")
    content = [x.split('do()') for x in content]
    content = content[00] + ["".join(x[1:]) for x in content[1:]]
    content = "".join(content)

    working = re.findall(pattern, content)
    total = sum(int(x[x.find('(') + 1:x.find(',')]) * int(x[x.find(',') + 1: x.find(')')]) for x in working)

    return total


if __name__ == "__main__":
    file = open(r'data/day_3/part_1.txt', 'r')
    _content = file.read()
    file.close()

    count = part_1(_content)
    print(count)

    count = part_2(_content)
    print(count)
