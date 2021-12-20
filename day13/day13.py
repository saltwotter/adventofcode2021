from os import sep


def find_coord_fold(fold_line, start):
    dist_from_line = start - fold_line - 1  # Account for fold line itself
    return fold_line - dist_from_line


def count_grid(grid):
    count = 0
    for x in grid:
        for y in x:
            if y == "X":
                count += 1
    return count


def find_boundaries(grid):
    x_val = []
    y_val = []
    for x, y in grid:
        x_val.append(int(x))
        y_val.append(int(y))
    return [max(x_val), max(y_val)]


def separate_out_coords(grid):
    return [z.split(",") for z in grid]


with open("day13/input", mode="r") as f:
    grid_marks, folds = [x.splitlines() for x in f.read().split("\n\n")]
    grid_marks = separate_out_coords(grid_marks)
    folds = [x[11:].split("=") for x in folds]

x_last, y_last = find_boundaries(grid_marks)

grid = [list("." * (x_last + 1)) for _ in range(y_last + 1)]

for xmark, ymark in grid_marks:
    grid[int(ymark)][int(xmark)] = "X"

fold_num = 1
for direction, line_num in folds:
    line_num = int(line_num)
    if direction == "y":
        temp = grid[:line_num]
        for yval, row in enumerate(grid):
            for xval, x in enumerate(row):
                if x == "X":
                    new_val = find_coord_fold(line_num, int(yval)) - 1
                    if new_val < line_num:
                        temp[new_val][xval] = x
    else:
        temp = [x[:line_num] for x in grid]
        for yval, row in enumerate(grid):
            for xval, x in enumerate(row):
                if x == "X":
                    new_val = find_coord_fold(line_num, int(xval)) - 1
                    if new_val < line_num:
                        temp[yval][new_val] = x
    grid = temp
    print(f"Fold {fold_num:2d}: {count_grid(grid)}")


for y in grid:
    line = ""
    for x in y:
        line += x
    print(line)
