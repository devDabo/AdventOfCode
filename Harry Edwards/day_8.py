from collections import defaultdict


def create_pairs(lst):
    if len(lst) == 1:
        return []

    pairs = [[lst[0], x] for x in lst[1:]]
    return pairs + create_pairs(lst[1:])


def on_map(coord, y_max, x_max):
    if 0 <= coord[0] < x_max and 0 <= coord[1] < y_max:
        return True
    else:
        return False


def part_1(content, y_max, x_max):
    all_antennas = [[v, k] for k, v in content.items() if v != "."]
    unique_values = set([v for v in content.values() if v != "."])

    antinodes = set()
    for value in unique_values:
        matching_pairs = create_pairs([x[1] for x in all_antennas if x[0] == value])

        for pair in matching_pairs:
            direction = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
            antinode_1 = (pair[0][0] + direction[0], pair[0][1] + direction[1])
            antinode_2 = (pair[1][0] - direction[0], pair[1][1] - direction[1])

            if on_map(antinode_1, y_max, x_max):
                antinodes.add(antinode_1)
            if on_map(antinode_2, y_max, x_max):
                antinodes.add(antinode_2)

    return len(antinodes)


def part_2(content, y_max, x_max):
    all_antennas = [[v, k] for k, v in content.items() if v != "."]
    unique_values = set([v for v in content.values() if v != "."])

    antinodes = set()
    for value in unique_values:
        matching_pairs = create_pairs([x[1] for x in all_antennas if x[0] == value])

        for pair in matching_pairs:
            direction = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])

            location = pair[0]
            while on_map(location, y_max, x_max):
                antinodes.add(location)
                location = (location[0] + direction[0], location[1] + direction[1])

            location = pair[1]
            while on_map(location, y_max, x_max):
                antinodes.add(location)
                location = (location[0] - direction[0], location[1] - direction[1])

    return len(antinodes)


if __name__ == "__main__":
    file = open(r'data/day_8/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _y_max = len(_content)
    _x_max = len(_content[0])

    _content = defaultdict(str) | {(x, y): val for y, row in enumerate(_content) for x, val in enumerate(row)}

    _count = part_1(_content, _y_max, _x_max)
    print(_count)

    _count = part_2(_content, _y_max, _x_max)
    print(_count)
