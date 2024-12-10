import math


def test_values_str(numbers):
    if len(numbers) == 1:
        return_value = [[numbers[-1]]]
    else:
        next_numbers = test_values_str(numbers[:-1])
        # return_value = [x + [op] + [numbers[-1]] for op in ['+', '*'] for x in next_numbers]
        return_value = [x + ["+"] + [numbers[-1]] for x in next_numbers] + [x + ["*"] + [numbers[-1]] for x in
                                                                            next_numbers]

    return return_value


def test_values(numbers: list):
    if len(numbers) == 1:
        return_value = [numbers[-1]]
    else:
        next_numbers = test_values(numbers[:-1])
        return_value = [sum([x] + [numbers[-1]]) for x in next_numbers] + [math.prod([x] + [numbers[-1]]) for x in
                                                                           next_numbers]

    return return_value

def test_values_2(numbers: list):
    if len(numbers) == 1:
        return_value = [numbers[-1]]
    else:
        next_numbers = test_values_2(numbers[:-1])
        return_value = ([sum([x] + [numbers[-1]]) for x in next_numbers] +
                        [math.prod([x] + [numbers[-1]]) for x in next_numbers] +
                        [int(str(x) + str(numbers[-1])) for x in next_numbers])

    return return_value


def part_1(content):
    total = 0
    for item in content:
        target = item[0]
        values = item[1]
        solutions = test_values(values)

        if target in solutions:
            total += target

    return total


def part_2(content):
    total = 0
    for item in content:
        target = item[0]
        values = item[1]
        solutions = test_values_2(values)

        if target in solutions:
            total += target

    return total


if __name__ == "__main__":
    file = open(r'data/day_7/part_1.txt', 'r')
    _content = file.read()
    file.close()

    _content = _content.replace("\n", "-").split("-")
    _content = [[x.split(':')[0], x.split(':')[1].strip()] for x in _content]
    _content = [[int(y[0]), [int(z) for z in y[1].split(' ')]] for y in _content]

    # _count = part_1(_content)
    # print(_count)

    _count = part_2(_content)
    print(_count)
