def horz_line(start, stop):
    xval = start[0]
    dist = abs(start[1] - stop[1])
    result = []
    if start[1] > stop[1]:
        for x in range(dist + 1):
            result.append(str(xval) + "," + str(start[1] - x))
    else:
        for x in range(dist + 1):
            result.append(str(xval) + "," + str(start[1] + x))
    return result


def vert_line(start, stop):
    yval = start[1]
    dist = abs(start[0] - stop[0])
    result = []
    if start[0] > stop[0]:
        for x in range(dist + 1):
            result.append(str(start[0] - x) + "," + str(yval))
    else:
        for x in range(dist + 1):
            result.append(str(start[0] + x) + "," + str(yval))
    return result


def string_to_coords(string):
    return [int(x) for x in string.split(",")]


def diag_line(start, stop):
    dist = abs(start[0] - stop[0])
    result = []
    if start[0] > stop[0] and start[1] > stop[1]:
        for x in range(dist + 1):
            result.append(str(start[0] - x) + "," + str(start[1] - x))
    elif start[0] > stop[0] and start[1] < stop[1]:
        for x in range(dist + 1):
            result.append(str(start[0] - x) + "," + str(start[1] + x))
    elif start[0] < stop[0] and start[1] > stop[1]:
        for x in range(dist + 1):
            result.append(str(start[0] + x) + "," + str(start[1] - x))
    else:
        for x in range(dist + 1):
            result.append(str(start[0] + x) + "," + str(start[1] + x))

    return result


def part1(inputs):
    vents = set()
    crossed = set()

    for line in inputs:
        start = string_to_coords(line[0])
        last = string_to_coords(line[1])
        if start[0] == last[0]:
            for x in horz_line(start, last):
                if x in vents:
                    crossed.add(x)
                else:
                    vents.add(x)

        elif start[1] == last[1]:
            for x in vert_line(start, last):
                if x in vents:
                    crossed.add(x)
                else:
                    vents.add(x)

    print(f"Overlays: {len(crossed)}")


def part2(inputs):
    vents = set()
    crossed = set()

    for line in inputs:
        start = string_to_coords(line[0])
        last = string_to_coords(line[1])
        if start[0] == last[0]:
            for x in horz_line(start, last):
                if x in vents:
                    crossed.add(x)
                else:
                    vents.add(x)

        elif start[1] == last[1]:
            for x in vert_line(start, last):
                if x in vents:
                    crossed.add(x)
                else:
                    vents.add(x)
        else:
            for x in diag_line(start, last):
                if x in vents:
                    crossed.add(x)
                else:
                    vents.add(x)

    print(f"Overlays: {len(crossed)}")


def main():
    with open("day5/input", mode="r") as f:
        inputs = [x.split(" -> ") for x in f.read().splitlines()]

    print("---Part 1---")
    part1(inputs)
    print("---Part 2---")
    part2(inputs)


if __name__ == "__main__":
    main()
