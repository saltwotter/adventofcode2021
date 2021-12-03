## Challenge 1

with open("day3/input", mode="r") as f:
    lines = f.read().splitlines()

binaries = [list() for i in range(len(lines[0]))]

for line in lines:
    for i, x in enumerate(line):
        binaries[i].append(int(x))

final = ""

for x in binaries:
    final += str(round(sum(x) / len(x)))

inverted = ""

for x in final:
    if x == "1":
        inverted += "0"
    else:
        inverted += "1"

print(int(final, 2))
print(int(inverted, 2))
print(int(final, 2) * int(inverted, 2))

## Challenge 2


def bit_to_check(bins, i):
    vals = [int(line[i]) for line in bins]
    if vals.count(1) == vals.count(0):
        return "1"
    elif vals.count(1) > vals.count(0):
        return "1"
    else:
        return "0"


oxy_kept = lines
oxy_temp = []

for x in range(len(final)):
    bit = bit_to_check(oxy_kept, x)
    for line in oxy_kept:
        if line[x] == bit:
            oxy_temp.append(line)
    oxy_kept = oxy_temp
    oxy_temp = []
    if len(oxy_kept) == 1:
        break

print(int(oxy_kept[0], 2))

co2_kept = lines
co2_temp = []

for x in range(len(final)):
    bit = "0" if bit_to_check(co2_kept, x) == "1" else "1"
    for line in co2_kept:
        if line[x] == bit:
            co2_temp.append(line)
    co2_kept = co2_temp
    co2_temp = []
    if len(co2_kept) == 1:
        break

print(int(co2_kept[0], 2))

print(int(co2_kept[0], 2) * int(oxy_kept[0], 2))
