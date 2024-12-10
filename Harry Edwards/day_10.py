from collections import defaultdict


def on_map(coord, x_max, y_max):
    if 0 <= coord[0] < x_max and 0 <= coord[1] < y_max:
        return True
    else:
        return False


def make_path(coords, grid, x_max, y_max, end_points):
    for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        position = (coords[0] + move[0], coords[1] + move[1])
        if on_map(position, x_max, y_max):
            if grid[position] - grid[coords] == 1:
                if grid[position] == 9:
                    end_points += [position]
                else:
                    make_path(position, grid, x_max, y_max, end_points)


def part_1(content, x_max, y_max):
    zeros = [coord for coord, val in content.items() if val == 0]

    paths = {}
    for zero in zeros:
        end_points = []
        make_path(zero, content, x_max, y_max, end_points)
        paths[zero] = end_points

    return sum(len(set(v)) for v in paths.values()), sum(len(v) for v in paths.values())


if __name__ == "__main__":
    file = open(r'data/day_10/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _max_x = len(_content)
    _max_y = len(_content[0])
    _content = defaultdict(str) | {(x, y): int(val) for y, row in enumerate(_content) for x, val in enumerate(row)}

    _part_1, _part_2 = part_1(_content, _max_x, _max_y)
    print(_part_1)
    print(_part_2)
