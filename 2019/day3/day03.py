def get_data():
    with open("input/input3.txt", "r") as f:
        lines = f.readlines()
        cavo1 = [(x[0], int(x[1:])) for x in lines[0].split(",")]
        cavo2 = [(x[0], int(x[1:])) for x in lines[1].split(",")]
    return cavo1, cavo2


def elabora_cavo(cavo):
    a = (0, 0)
    path_a = []
    for d, c in cavo:
        if "R" == d:
            for i in range(c):
                a = a[0], a[1] + 1
                path_a.append(a)
        if "L" == d:
            for i in range(c):
                a = a[0], a[1] - 1
                path_a.append(a)
        if "U" == d:
            for i in range(c):
                a = a[0] + 1, a[1]
                path_a.append(a)
        if "D" == d:
            for i in range(c):
                a = a[0] - 1, a[1]
                path_a.append(a)
    return path_a


if __name__ == "__main__":
    a, b = get_data()
    path_a = elabora_cavo(a)
    path_b = elabora_cavo(b)
    print(path_a)
    print(path_b)
    in_common = list(set(path_a).intersection(path_b))
    output = []
    for a, b in in_common:
        output.append(abs(a) + abs(b))
    output.sort()
    print(output[0])

    output2 = []
    for element in in_common:
        output2.append(path_a.index(element) + 2 + path_b.index(element))
    output2.sort()
    print(output2)
