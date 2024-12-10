from collections import defaultdict


def get_diags(content):
    new_content = []
    for x in range(len(content[0])):
        for y in range(len(content)):
            if (x + 3 < len(content[0])) & (y + 3 < len(content)):
                new_content += [content[y][x] + content[y + 1][x + 1] + content[y + 2][x + 2] + content[y + 3][x + 3]]

    return new_content


def get_verts(content):
    new_content = []
    for x in range(len(content[0])):
        for y in range(len(content)):
            if y + 3 < len(content):
                new_content += [content[y][x] + content[y + 1][x] + content[y + 2][x] + content[y + 3][x]]

    return new_content


def get_horzs(content):
    new_content = []
    for x in range(len(content[0])):
        for y in range(len(content)):
            if x + 3 < len(content):
                new_content += [content[y][x] + content[y][x + 1] + content[y][x + 2] + content[y][x + 3]]

    return new_content


def part_1(content):
    content = [list(x) for x in content]

    across_r2l = sum(1 for x in get_horzs(content) if x == "XMAS")
    across_l2r = sum(1 for x in get_horzs([y[::-1] for y in content]) if x == "XMAS")

    diag_0 = sum(1 for x in get_diags(content) if x == "XMAS")
    diag_90 = sum(1 for x in get_diags(list(zip(*content[::-1]))) if x == "XMAS")
    diag_180 = sum(1 for x in get_diags([y[::-1] for y in content[::-1]]) if x == "XMAS")
    diag_270 = sum(1 for x in get_diags(list(zip(*content))[::-1]) if x == "XMAS")

    vert_u2d = sum(1 for x in get_verts(content) if x == "XMAS")
    vert_d2u = sum(1 for x in get_verts(content[::-1]) if x == "XMAS")

    return across_l2r + across_r2l + diag_0 + diag_90 + diag_180 + diag_270 + vert_u2d + vert_d2u


def part_2(content):
    content = [list(x) for x in content]
    content = defaultdict(str) | {(i, j): col for i, row in enumerate(content) for j, col in enumerate(row)}

    check = (-1, 0, 1)
    coords = list(content.keys())
    hit = [list(x) for x in ['MAS', 'SAM']]

    count = sum([content[y + delta, x + delta] for delta in check] in hit and
                [content[y + delta, x - delta] for delta in check] in hit for x, y in coords)

    return count


if __name__ == "__main__":
    file = open(r'data/day_4/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    # count = part_1(_content)
    # print(count)

    count = part_2(_content)
    print(count)
