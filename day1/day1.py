## Challenge 1

with open("day1/input", "r") as file:
    day1 = file.readlines()

day1 = [int(x) for x in day1]
increased = 0

for i, x in enumerate(day1):
    if i:
        if x > day1[i - 1]:
            increased += 1

print(increased)

## Challenge 2

increased = 0

for i, x in enumerate(day1):
    if not i < 2:
        sum1 = x + day1[i - 1] + day1[i - 2]
        sum2 = day1[i - 1] + day1[i - 2] + day1[i - 3]
        if sum1 > sum2:
            increased += 1

print(increased)
