from math import ceil


def separate_symbols(pairs):
    result = {}
    for pair in pairs:
        if pair[0] in result:
            result[pair[0]] += pairs[pair]
        else:
            result[pair[0]] = pairs[pair]
        if pair[1] in result:
            result[pair[1]] += pairs[pair]
        else:
            result[pair[1]] = pairs[pair]
    for sym in result:
        result[sym] = ceil(result[sym] / 2)
    return result


with open("day14/input", mode="r") as f:
    template, rules = f.read().split("\n\n")
    rule_strings = [x.split(" -> ") for x in rules.splitlines()]

rules = {}
steps = 40
pairs = {}

for pair, center in rule_strings:
    rules[pair] = center

for x in range(len(template) - 1):
    pair = template[x] + template[x + 1]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

for run in range(steps):
    print(f"Step {run + 1:2d}")
    temp = {}
    for pair in pairs:
        new1 = pair[0] + rules[pair]
        new2 = rules[pair] + pair[1]
        if new1 in temp:
            temp[new1] += pairs[pair]
        else:
            temp[new1] = pairs[pair]
        if new2 in temp:
            temp[new2] += pairs[pair]
        else:
            temp[new2] = pairs[pair]
    pairs = temp

symbs = separate_symbols(pairs)

print(f"Min: {min(symbs.values())}\nMax: {max(symbs.values())}")
print(f"Answer: {max(symbs.values()) - min(symbs.values())}")
