def part_1(content):
    disk = []
    for n in range(0, len(content), 2):
        pos = n / 2
        if pos == int(len(content) / 2):
            disk += [int(pos) for _ in range(content[n])]
        else:
            disk += [int(pos) for _ in range(content[n])] + ["." for _ in range(content[n + 1])]

    n = 0
    while (n < len(disk)) & (len([x for x in disk[n:] if x != "."]) > 0):
        if disk[n] == ".":
            far_right_index = len(disk) - next(i for i, x in enumerate(disk[::-1]) if x != ".") - 1
            disk[n] = disk[far_right_index]
            disk[far_right_index] = "."
        n += 1

    return sum(n * x for n, x in enumerate(disk) if x != ".")


def part_2(content):
    disk = []
    for n in range(0, len(content), 2):
        pos = n / 2
        if pos == int(len(content) / 2):
            disk += [(int(pos), content[n])]
        else:
            disk += [(int(pos), content[n]), (".", content[n + 1])]

    for pos in range(disk[-1][0], 1, -1):
        n = [i for i, x in enumerate(disk) if x[0] == pos][0]
        if disk[n][0] == ".":
            continue
        else:
            for m in range(len(disk)):
                if n <= m:
                    break
                if disk[m][0] == "." and disk[m][1] >= disk[n][1]:
                    if disk[m][1] == disk[n][1]:
                        disk[m] = disk[n]
                        disk[n] = (".", disk[m][1])
                    else:
                        new_space_size, drop_forwards, drop_back = disk[n][1], 0, 0
                        if n + 1 < len(disk):
                            if disk[n + 1][0] == ".":
                                new_space_size += disk[n + 1][1]
                                drop_forwards = 1
                        if disk[n - 1][0] == ".":
                            new_space_size += disk[n - 1][1]
                            drop_back = 1

                        disk = disk[:m] + [disk[n]] + [(".", disk[m][1] - disk[n][1])] + disk[m + 1:n-drop_back] + [
                            (".", new_space_size)] + disk[n + 1 + drop_forwards:]
                    break

    pos = 0
    checksum = 0
    for n in range(0, len(disk)):
        pos += disk[n][1]
        if disk[n][0] != ".":
            checksum += sum(disk[n][0] * i for i in range(pos - disk[n][1], pos))

    return checksum


if __name__ == "__main__":
    file = open(r'data/day_9/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _content = [int(x) for x in _content[0]]

    _count = part_1(_content)
    print(_count)

    _count = part_2(_content)
    print(_count)
