def part_1(content):
    count = 0

    for y in content:
        mono_inc = all(y[n] < y[n + 1] for n in range(len(y) - 1))
        mono_dec = all(y[n] > y[n + 1] for n in range(len(y) - 1))
        mono = mono_inc | mono_dec

        diff = all((abs(y[n] - y[n + 1]) >= 1) & (abs(y[n] - y[n + 1]) <= 3) for n in range(len(y) - 1))

        if diff & mono:
            count += 1

    return count


def part_2(content):
    count = 0

    for y in content:
        mono = []
        diff = []
        for i in range(len(y)):
            y_new = y[:i] + y[i + 1:]
            mono_inc = all(y_new[n] < y_new[n + 1] for n in range(len(y_new) - 1))
            mono_dec = all(y_new[n] > y_new[n + 1] for n in range(len(y_new) - 1))
            mono += [mono_inc | mono_dec]

            diff += [all((abs(y_new[n] - y_new[n + 1]) >= 1) & (abs(y_new[n] - y_new[n + 1]) <= 3) for n in
                         range(len(y_new) - 1))]

        x = sum(x * y for x, y in zip(mono, diff))
        if sum(x * y for x, y in zip(mono, diff)) > 0:
            count += 1

    return count


if __name__ == "__main__":
    file = open(r'data/day_2/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _content = [[int(x) for x in y.split(" ")] for y in _content]

    count = part_1(_content)
    print(count)

    count = part_2(_content)
    print(count)
