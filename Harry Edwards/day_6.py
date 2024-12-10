from collections import defaultdict


def part_1(content):
    x_max = len(content[0])
    y_max = len(content)

    map = defaultdict(str) | {(x, y): col for y, row in enumerate(content) for x, col in enumerate(row)}

    location = [k for k, v in map.items() if v == '^'][0]
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_index = 0

    passed = set()
    while (location[0] >= 0) & (location[0] < x_max) & (location[1] >= 0) & (location[1] < y_max):
        if map[location] == "#":
            location = (location[0] - directions[direction_index][0], location[1] - directions[direction_index][1])
            direction_index = (direction_index + 1) % 4
            location = (location[0] + directions[direction_index][0], location[1] + directions[direction_index][1])
        else:
            passed.add(location)
            location = (location[0] + directions[direction_index][0], location[1] + directions[direction_index][1])

    return len(passed), map, passed, y_max, x_max


def part_2(map, passed, y_max, x_max):
    start = [k for k, v in map.items() if v == '^'][0]
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    count = 0

    for n, spot in enumerate(passed):
        direction_index, steps, loop = 0, [], True
        location = start
        loop_map = map.copy()
        loop_map[spot] = '#'

        while (location[0] >= 0) & (location[0] < x_max) & (location[1] >= 0) & (location[1] < y_max) & loop:
            if loop_map[location] == "#":
                location = (location[0] - directions[direction_index][0], location[1] - directions[direction_index][1])
                direction_index = (direction_index + 1) % 4
                location = (location[0] + directions[direction_index][0], location[1] + directions[direction_index][1])
            else:
                steps += [(location[0], location[1], direction_index)]
                location = (location[0] + directions[direction_index][0], location[1] + directions[direction_index][1])

            if (location[0], location[1], direction_index) in steps:
                count += 1
                loop = False

    return count


if __name__ == "__main__":
    file = open(r'data/day_6/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _count, _map, _passed, _y_max, _x_max = part_1(_content)
    print(_count)

    _count = part_2(_map, _passed, _y_max, _x_max)
    print(_count)
