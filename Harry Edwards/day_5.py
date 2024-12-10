def part_1(rules, pages):
    print_list = []
    for page in pages:
        for n, rule in enumerate(rules):
            if n < len(rules) - 1:
                if (rule[0] not in page) | (rule[1] not in page):
                    continue
                elif page.index(rule[0]) > page.index(rule[1]):
                    break
            else:
                if ((rule[0] not in page) | (rule[1] not in page)):
                    print_list += [page]
                elif (page.index(rule[0]) < page.index(rule[1])):
                    print_list += [page]

    total = sum(x[int(len(x) / 2)] for x in print_list)

    return total


def part_2(rules, pages):
    wrong_list = []
    for page in pages:
        page_orig = page.copy()
        for n, rule in enumerate(rules):
            if (rule[0] not in page) | (rule[1] not in page):
                continue
            elif page.index(rule[0]) > page.index(rule[1]):
                reorder, m = True, 0
                app_rules = [r for r in rules if r[0] in page and r[1] in page]
                while reorder:
                    page_prev = page.copy()
                    for r in app_rules:
                        if page.index(r[0]) > page.index(r[1]):
                            i, j = page.index(r[0]), page.index(r[1])
                            page[i], page[j] = page[j], page[i]
                    if page_prev == page:
                        reorder = False
                break

        if page_orig != page:
            wrong_list += [page]


    total = sum(x[int(len(x) / 2)] for x in wrong_list)
    return total


if __name__ == "__main__":
    file = open(r'data/day_5/part_1.txt', 'r')
    _content = file.read().replace("\n", "-").split("-")
    file.close()

    _rules = [[int(y) for y in x.split("|")] for x in _content[:_content.index('')]]
    _pages = [[int(y) for y in x.split(',')] for x in _content[_content.index('') + 1:]]

    # count = part_1(_rules, _pages)
    # print(count)

    count = part_2(_rules, _pages)
    print(count)
