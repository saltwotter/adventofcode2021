## Challenge 1


class Submarine:
    def __init__(self):
        self.h_position = 0
        self.depth = 0

    def forward(self, n):
        self.h_position += n

    def up(self, n):
        self.depth -= n

    def down(self, n):
        self.depth += n

    def result(self):
        return self.h_position * self.depth


with open("day2/input") as f:
    lines = f.readlines()

sub = Submarine()

for line in lines:
    command, num = line.split()

    if command == "forward":
        sub.forward(int(num))
    elif command == "up":
        sub.up(int(num))
    elif command == "down":
        sub.down(int(num))

print(sub.result())

## Challenge 2


class SubAim(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, n):
        self.h_position += n
        self.depth += self.aim * n

    def up(self, n):
        self.aim -= n

    def down(self, n):
        self.aim += n


sub = SubAim()

for line in lines:
    command, num = line.split()

    if command == "forward":
        sub.forward(int(num))
    elif command == "up":
        sub.up(int(num))
    elif command == "down":
        sub.down(int(num))

print(sub.result())
