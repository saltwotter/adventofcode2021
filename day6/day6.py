class LanternFish:
    def __init__(self, cycle_day=9):
        self.cycle_day = cycle_day

    def add_day(self):
        if self.cycle_day == 0:
            self.cycle_day = 7
        self.cycle_day -= 1

    def check_gestation(self):
        return self.cycle_day == 0

    def offspring(self):
        return LanternFish()


def exp_main():
    DAYS = 80

    with open("day6/input", mode="r") as f:
        inputs = [int(x) for x in f.read().strip().split(",")]

    fishes = []
    new_fish = []

    for x in inputs:
        fishes.append(LanternFish(x))
    print(f"Day {0:2d}: {len(fishes):4d} -- {[x.cycle_day for x in fishes]}")

    for x in range(DAYS):
        for fish in fishes:
            fish.add_day()
        print(f"Day {x + 1:2d}: {len(fishes):4d}")
        new_fish = []
        for fish in fishes:
            if fish.check_gestation():
                new_fish.append(fish.offspring())
        fishes += new_fish


def sum_dict(d):
    result = 0
    for i in d:
        result += d[i]
    return result


def ox_main():
    DAYS = 256
    fishes = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}

    with open("day6/input", mode="r") as f:
        inputs = [int(x) for x in f.read().strip().split(",")]

    for x in inputs:
        fishes[x] += 1

    for x in range(DAYS + 1):
        print(f"Day {x:2d}: {sum_dict(fishes)}")
        new_fishes = 0
        for day in range(len(fishes)):
            if day == 0:
                new_fishes += fishes[day]
            else:
                fishes[day - 1] = fishes[day]
        fishes[6] += new_fishes
        fishes[8] = new_fishes


if __name__ == "__main__":
    # exp_main()
    ox_main()
