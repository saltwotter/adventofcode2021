def char_freq(string):
    result = {}
    for x in string:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result


with open("day14/input", mode="r") as f:
    template, rules = f.read().split("\n\n")
    rule_strings = [x.split(" -> ") for x in rules.splitlines()]

rules = {}
steps = 10

for pair, center in rule_strings:
    rules[pair] = center

for run in range(steps):
    result = ""
    for x in range(len(template) - 1):
        pair = template[x] + template[x + 1]
        result += pair[0] + rules[pair]
        if x == len(template) - 2:
            result += pair[1]
    template = result
    print(f"Step {run + 1}")

freqs = char_freq(template)
print(f"Min: {min(freqs.values())}\nMax: {max(freqs.values())}")
print(f"Answer: {max(freqs.values()) - min(freqs.values())}")
