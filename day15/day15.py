from queue import PriorityQueue


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def traverse(grid):
    lower_bound = len(grid)
    right_bound = len(grid[0])
    end = (lower_bound - 1, right_bound - 1)
    start = (0, 0)
    traversing = PriorityQueue()
    costs = {start: 0}
    history = set()
    history.add(start)
    offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))
    traversing.put((0, start))

    while not traversing.empty():
        position = traversing.get()[1]
        if position == end:
            break
        for offset in offsets:
            new = (position[0] + offset[0], position[1] + offset[1])
            if 0 <= new[0] < lower_bound and 0 <= new[1] < right_bound:
                new_cost = costs[position] + grid[position[1]][position[0]]
                if new not in history or new_cost < costs[new]:
                    costs[new] = new_cost
                    priority = new_cost + distance(new, end)
                    traversing.put((priority, new))
                    history.add(new)
    return costs[position]


with open("day15/input", mode="r") as f:
    inputs = [[int(x) for x in y] for y in f.read().splitlines()]

print("--- Part 1 ---")
print(traverse(inputs))

print("--- Part 2 ---")
og_depth = len(inputs)
og_width = len(inputs[0])
for i in range(4):
    for row in inputs:
        right = [x % 9 + 1 for x in row[-og_width:]]
        row.extend(right)
    for line in inputs[og_depth * i : og_depth * (i + 1)]:
        down = [x % 9 + 1 for x in line]
        inputs.append(down)

print(traverse(inputs))
