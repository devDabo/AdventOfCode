def get_numbers(frase: str) -> tuple[int, int]:
    result = (int(frase[frase.find("X") + 2:frase.find(",")]), int(frase[frase.find("Y") + 2:]))

    return result


def part_1(content):
    cost, cost_2 = 0, 0
    for game in content:
        A, B, P = game
        determinant = A[0] * B[1] - A[1] * B[0]

        if determinant == 0:
            continue

        M = ((B[1] * P[0] - B[0] * P[1]) / determinant, (A[0] * P[1] - A[1] * P[0]) / determinant)

        P = (P[0] + 10000000000000, P[1] + 10000000000000)
        M_2 = ((B[1] * P[0] - B[0] * P[1]) / determinant, (A[0] * P[1] - A[1] * P[0]) / determinant)

        if int(M_2[0]) == M_2[0] and int(M_2[1]) == M_2[1] and 0 <= M[0] <= 100 and 0 <= M[1] <= 100:
            cost += M[0] * 3 + M[1]
        if int(M_2[0]) == M_2[0] and int(M_2[1]) == M_2[1] and 0 <= M_2[0] and 0 <= M_2[1]:
            cost_2 += M_2[0] * 3 + M_2[1]

    return int(cost), int(cost_2)


if __name__ == "__main__":
    file = open(r'data/day_13/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _content = [x for x in _content if x != ""]
    _content = [_content[n:n + 3] for n in range(0, len(_content), 3)]
    _content = [[get_numbers(y) for y in x] for x in _content]

    _count, _count_2 = part_1(_content)
    print(_count)
    print(_count_2)
