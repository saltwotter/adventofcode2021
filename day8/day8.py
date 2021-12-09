### PART 1 ###
print("\n--- Part 1 ---")

with open("day8/input", mode="r") as f:
    inputs = [x.split(" | ") for x in f.read().strip().splitlines()]
    inputs = [[x.split(" ") for x in y] for y in inputs]

running = 0

for sets in inputs:
    for x in sets[1]:
        if len(x) in [2, 3, 4, 7]:
            running += 1

print(running)

### PART 2 ###
print("\n--- Part 2 ---")


class Digits:
    def __init__(self, obf_nums, obf_value):
        self.obf_nums = [set([y for y in x]) for x in obf_nums]
        self.obf_value = [set([y for y in x]) for x in obf_value]
        self.value = 0
        self.mapping = dict()

    def find_easy(self):
        for num in self.obf_nums:
            if len(num) == 2:
                self.mapping[1] = num
            elif len(num) == 3:
                self.mapping[7] = num
            elif len(num) == 4:
                self.mapping[4] = num
            elif len(num) == 7:
                self.mapping[8] = num

    def find_6(self):
        for num in self.obf_nums:
            if len(num) == 6 and not num.issuperset(self.mapping[1]):
                self.mapping[6] = num

    def find_5(self):
        for num in self.obf_nums:
            if len(num) == 5 and len(self.mapping[6] - num) == 1:
                self.mapping[5] = num

    def find_2(self):
        for num in self.obf_nums:
            if len(num) == 5 and len(self.mapping[5] ^ num) == 4:
                self.mapping[2] = num

    def find_9_0(self):
        for num in self.obf_nums:
            if (
                len(num) == 6
                and len(num - self.mapping[5]) == 1
                and num != self.mapping[6]
            ):
                self.mapping[9] = num
            elif len(num) == 6 and num != self.mapping[6]:
                self.mapping[0] = num

    def find_3(self):
        for num in self.obf_nums:
            if num not in self.mapping.values():
                self.mapping[3] = num

    def find_all(self):
        self.find_easy()
        self.find_6()
        self.find_5()
        self.find_2()
        self.find_9_0()
        self.find_3()

    def calculate(self):
        self.find_all()
        result = ""
        for obf in self.obf_value:
            for map in self.mapping:
                if self.mapping[map] == obf:
                    result += str(map)
        self.value = int(result)
        return self.value


puzzles = [Digits(x, y) for x, y in inputs]
print(sum([x.calculate() for x in puzzles]))
