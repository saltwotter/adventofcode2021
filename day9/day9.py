with open("day9/input", mode="r") as f:
    inputs = f.read().splitlines()
    inputs = [[int(y) for y in x] for x in inputs]

### PART 1 ###
print("--- Part 1 ---")

x_len = len(inputs[0])
y_len = len(inputs)
lowests = []

for y_val, y in enumerate(inputs):
    for x_val, x in enumerate(y):
        to_check = []
        if 0 < y_val:
            to_check.append(inputs[y_val - 1][x_val])
        if y_val < y_len - 1:
            to_check.append(inputs[y_val + 1][x_val])
        if 0 < x_val:
            to_check.append(inputs[y_val][x_val - 1])
        if x_val < x_len - 1:
            to_check.append(inputs[y_val][x_val + 1])
        lowest = True
        for n in to_check:
            if x >= n:
                lowest = False
        if lowest:
            lowests.append(x)

print(sum([x + 1 for x in lowests]))

### PART 2 ###
print("--- Part 2 ---")

heightmap = [[0 if num != 9 else 9 for num in line] for line in inputs]


# Could not wrap mind around problem, adapted from another solution
def floodfill(matrix, x, y):
    score = 0
    if matrix[y][x] == 0:
        matrix[y][x] = 1
        score = 1
        if x > 0:
            score += floodfill(matrix, x - 1, y)
        if x < len(matrix[0]) - 1:
            score += floodfill(matrix, x + 1, y)
        if y > 0:
            score += floodfill(matrix, x, y - 1)
        if y < len(matrix) - 1:
            score += floodfill(matrix, x, y + 1)
    return score


scores = []
for idx in range(x_len):
    for jdx in range(y_len):
        scores.append(floodfill(heightmap, idx, jdx))

scores = sorted(scores, reverse=True)[:3]

print(scores[0] * scores[1] * scores[2])
