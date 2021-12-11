class Sub:
    def __init__(self, inputs):
        self.inputs = inputs
        self.chars = []
        self.MAPPING = {"[": "]", "{": "}", "(": ")", "<": ">"}
        self.is_corrupt = False
        self.is_incomplete = False

    def closing(self, char):
        to_check = self.chars.pop()
        if char != self.MAPPING[to_check]:
            return False
        return True

    def open(self, char):
        self.chars.append(char)

    def verify_corrupt(self):
        self.chars = []
        for x in self.inputs:
            if x in ["(", "[", "{", "<"]:
                self.open(x)
            else:
                if not self.closing(x):
                    self.is_corrupt = True
                    return x

    def verify_incomplete(self):
        self.chars = []
        for x in self.inputs:
            if x in ["(", "[", "{", "<"]:
                self.open(x)
            else:
                self.closing(x)
        if len(self.chars) != 0:
            self.is_incomplete = True

    def complete(self):
        completers = []
        for x in self.chars[::-1]:
            completers.append(self.MAPPING[x])
        return completers


CORRUPT_SCORING = {")": 3, "]": 57, "}": 1197, ">": 25137}
INCOMPL_SCORING = {")": 1, "]": 2, "}": 3, ">": 4}


with open("day10/input", mode="r") as f:
    inputs = f.read().splitlines()

lines = []
score_corrupt = 0
scores_complete = []

for pairs in inputs:
    pair = Sub(pairs)
    pog = pair.verify_corrupt()
    if pog:
        score_corrupt += CORRUPT_SCORING[pog]
    if not pair.is_corrupt:
        pair.verify_incomplete()
    if pair.is_incomplete:
        temp_score = 0
        for char in pair.complete():
            temp_score *= 5
            temp_score += INCOMPL_SCORING[char]
        scores_complete.append(temp_score)

scores_complete.sort()

### PART 1 ###
print("--- Part 1 ---")
print(score_corrupt)

### PART 2 ###
print("--- Part 2 ---")
print(scores_complete[int(len(scores_complete) / 2)])
