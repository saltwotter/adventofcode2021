class Cave:
    def __init__(self, letter):
        self.is_small = False
        self.is_large = False
        self.connections = []
        if letter.isupper():
            self.is_large = True
        else:
            self.is_small = True

    def add_connection(self, connection):
        self.connections.append(connection)

    def has_connection(self, connector):
        if connector in self.connections:
            return True
        return False


def explore(cave, caves, traversed, working_string, strings, twice_visit=False):
    for c in caves[cave].connections:
        if c == "end":
            working_string += "end"
            strings.append(working_string)
        elif (caves[c].is_small and c in traversed and twice_visit) or c == "start":
            pass
        elif caves[c].is_small and c in traversed and not twice_visit:
            explore(
                c,
                caves,
                traversed + [c],
                working_string + f"{c},",
                strings,
                twice_visit=True,
            )
        else:
            explore(
                c,
                caves,
                traversed + [c],
                working_string + f"{c},",
                strings,
                twice_visit,
            )


with open("day12/input", mode="r") as f:
    inputs = [x.split("-") for x in f.read().splitlines()]

caves = {}

for c1, c2 in inputs:
    if c1 not in caves:
        caves[c1] = Cave(c1)
    if c2 not in caves:
        caves[c2] = Cave(c2)
    caves[c1].add_connection(c2)
    caves[c2].add_connection(c1)

paths = []
for cave in caves["start"].connections:
    explore(cave, caves, ["start", cave], f"start,{cave},", paths)

print(len(paths))
