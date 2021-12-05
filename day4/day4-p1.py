import re


class Bingo:
    def __init__(self, board):
        self.ROWS = 5
        self.COLUMNS = 5
        self.board = [[], [], [], [], []]
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                self.board[row].append({"num": board.pop(0), "called": False})

    def __str__(self):
        result = ""
        for row in self.board:
            for i, column in enumerate(row):
                result += f"{column['num']:2d}"
                result += "T" if column["called"] else "F"
                result += " " if i < len(row) - 1 else "\n"
        return result

    def check_rows(self):
        for row in self.board:
            row_hits = 0
            for column in row:
                row_hits += 1 if column["called"] else 0
            if row_hits == self.ROWS:
                return True
        return False

    def check_columns(self):
        for column in range(self.COLUMNS):
            col_hits = 0
            for row in self.board:
                col_hits += 1 if row[column]["called"] else 0
            if col_hits == self.COLUMNS:
                return True
        return False

    def find_hit(self, num):
        for row in self.board:
            for column in row:
                if column["num"] == num:
                    column["called"] = True

    def summation(self):
        result = 0
        for row in self.board:
            for column in row:
                if not column["called"]:
                    result += column["num"]
        return result


def process_board(inputs):
    results = []
    for line in inputs:
        results += [int(x) for x in re.split(r"\s+", line.lstrip())]
    return results


def check_boards(boards):
    for i, board in enumerate(boards):
        if board.check_columns() or board.check_rows():
            return i


def find_hits(boards, n):
    for board in boards:
        board.find_hit(n)


def main():
    with open("day4/input", mode="r") as f:
        inp = f.read().splitlines()

    calls = [int(x) for x in inp.pop(0).split(",")]
    inp.pop(0)

    # process boards
    boards = []
    board_wk = []
    while len(inp) > 0:
        current = inp.pop(0)
        if current == "":
            boards.append(Bingo(process_board(board_wk)))
            board_wk = []
        elif len(inp) == 0:
            board_wk.append(current)
            boards.append(Bingo(process_board(board_wk)))
        else:
            board_wk.append(current)

    # Begin Game!
    current_num = 0

    while len(calls) > 0:
        current_num = calls.pop(0)
        find_hits(boards, current_num)
        winner = check_boards(boards)
        if winner:
            print(f"Bingo! Board {winner + 1}.")
            print(f"Summation: {boards[winner].summation()}")
            print(f"Current Number: {current_num}")
            print(f"Final Score: {boards[winner].summation() * current_num}")
            break


if __name__ == "__main__":
    main()
