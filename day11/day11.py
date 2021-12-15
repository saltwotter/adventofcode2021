def print_matrix(matrix):
    for x in matrix:
        row = ""
        for y in x:
            row += str(y)
        print(row)


def get_neighbors(matrix, row, column):
    neighbors = []
    for y in range(column - 1, column + 2):
        if y >= 0 and y < len(matrix):
            for x in range(row - 1, row + 2):
                if x >= 0 and x < len(matrix[0]) and (x, y) != (row, column):
                    neighbors.append((x, y))
    return neighbors


def up_energy(matrix):
    to_check = []
    count = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] += 1
            if matrix[x][y] > 9:
                to_check.append((x, y))

    while len(to_check) > 0:
        checking = to_check.pop(0)
        if matrix[checking[0]][checking[1]] > 9:
            count += 1
            matrix[checking[0]][checking[1]] = 0
            for x, y in get_neighbors(matrix, checking[0], checking[1]):
                if matrix[x][y] != 0:
                    matrix[x][y] += 1
                if matrix[x][y] > 9:
                    to_check.append((x, y))
    return count


with open("day11/input", mode="r") as f:
    inputs = [[int(x) for x in y] for y in f.read().splitlines()]

### PART 1 ###
print("--- Part 1 ---")
ITERS = 100
blinks = 0

for i in range(ITERS):
    counted = up_energy(inputs)
    blinks += counted

print(f"Total Blinks: {blinks}")

with open("day11/input", mode="r") as f:
    inputs = [[int(x) for x in y] for y in f.read().splitlines()]

### PART 2 ###
print("--- Part 2 ---")
all_flashed = False
counter = 0

while not all_flashed:
    counted = up_energy(inputs)
    counter += 1
    if counted == len(inputs) * len(inputs[0]):
        print(f"All Flashed: Step {counter}")
        all_flashed = True
