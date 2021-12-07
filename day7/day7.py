with open("day7/input", mode="r") as f:
    inputs = [int(x) for x in f.read().strip().split(",")]

crabs = {}

for crab in inputs:
    if crab in crabs:
        crabs[crab] += 1
    else:
        crabs[crab] = 1

### PART 1 ###
print("--- Part 1 ---")

fuels = []

for pos1 in crabs:
    total = 0
    for pos2 in crabs:
        total += abs(pos2 - pos1) * crabs[pos2]
    print(f"Crab {pos1:8d}: {total}")
    fuels.append(total)

print(f"Fuel Efficiency: {min(fuels)}")

### PART 2 ###
print("--- Part 2 ---")

min_c = min(inputs)
max_c = max(inputs)
fuels = []

for pos1 in range(max_c - min_c + 1):
    total = 0
    for pos2 in crabs:
        dist = abs(pos2 - pos1)
        total += (((dist ** 2) + dist) / 2) * crabs[pos2]
    print(f"Pos {pos1:4d}: {int(total)}")
    fuels.append(total)

print(f"Fuel Efficiency: {int(min(fuels))}")
