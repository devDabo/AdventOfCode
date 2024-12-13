from collections import defaultdict


def find_region(position, max_x, max_y, plant, grid, region):
    if (position[0] >= 0 or position[0] < max_x) and (position[1] >= 0 or position[1] < max_y):
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_position = (position[0] + move[0], position[1] + move[1])
            if grid[next_position] == plant and next_position not in region:
                region += [next_position]
                find_region(next_position, max_x, max_y, plant, grid, region)


def count_vertices(positions: list):
    vertices = 0
    match len(positions):
        case 4:
            vertices += 4
        case 3:
            vertices += 2
        case 2:
            plant_1, plant_2 = positions[0], positions[1]
            if abs(plant_1[0] - plant_2[0]) == 1 and abs(plant_1[1] - plant_2[1]) == 1:
                vertices += 1
    return vertices


def part_1(grid, max_x, max_y):
    visited = set()

    coordinates = list(grid.keys())
    regions = []
    for position in coordinates:
        if position not in visited:
            region = [position]
            find_region(position, max_x, max_y, grid[position], grid, region)
            regions += [region]
            visited = visited.union(set(region))

    price_1 = 0
    for region in regions:
        perimeter = 0
        for position in region:
            for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_position = (position[0] + move[0], position[1] + move[1])
                if next_position not in region:
                    perimeter += 1
        price_1 += perimeter * len(region)

    price_2, outer_region, inner_region = 0, defaultdict(list), defaultdict(list)
    for region in regions:
        sides = 0
        outer_region.clear()
        inner_region.clear()
        for position in region:
            # Outer corner
            if (position[0] + 1, position[1]) not in region and (position[0], position[1] + 1) not in region:
                sides += 1
            if (position[0] - 1, position[1]) not in region and (position[0], position[1] + 1) not in region:
                sides += 1
            if (position[0] + 1, position[1]) not in region and (position[0], position[1] - 1) not in region:
                sides += 1
            if (position[0] - 1, position[1]) not in region and (position[0], position[1] - 1) not in region:
                sides += 1
            # Inner corner
            if (position[0] + 1, position[1]) in region and (position[0], position[1] + 1) in region and (
                    position[0] + 1, position[1] + 1) not in region:
                sides += 1
            if (position[0] - 1, position[1]) in region and (position[0], position[1] + 1) in region and (
                    position[0] - 1, position[1] + 1) not in region:
                sides += 1
            if (position[0] + 1, position[1]) in region and (position[0], position[1] - 1) in region and (
                    position[0] + 1, position[1] - 1) not in region:
                sides += 1
            if (position[0] - 1, position[1]) in region and (position[0], position[1] - 1) in region and (
                    position[0] - 1, position[1] - 1) not in region:
                sides += 1

        price_2 += sides * len(region)

    return price_1, price_2


if __name__ == "__main__":
    file = open(r'data/day_12/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _max_x = len(_content[0])
    _max_y = len(_content)
    _content = defaultdict(str) | {(x, y): val for y, row in enumerate(_content) for x, val in enumerate(row)}

    _count = part_1(_content, _max_x, _max_y)
    print(_count[0])
    print(_count[1])
