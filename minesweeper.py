import random

class MinesweeperGame:
    def __init__(self, rows=8, columns=8, mines=10):
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.board = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.hidden_board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.revealed_board = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.remaining_cells = rows * columns - mines
        self.generate_mines()

    def generate_mines(self):
        positions = [(r, c) for r in range(self.rows) for c in range(self.columns)]
        random.shuffle(positions)
        for r, c in positions[:self.mines]:
            self.hidden_board[r][c] = '*'
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= r + dr < self.rows and 0 <= c + dc < self.columns:
                        if self.hidden_board[r + dr][c + dc] != '*':
                            self.hidden_board[r + dr][c + dc] += 1

    def display_board(self):
        for row in self.revealed_board:
            print(' '.join(str(cell) for cell in row))

    def reveal_cell(self, row, col):
        if self.revealed_board[row][col] != ' ':
            return False
        if self.hidden_board[row][col] == '*':
            return True
        self.remaining_cells -= 1
        self.revealed_board[row][col] = self.hidden_board[row][col]
        if self.hidden_board[row][col] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= row + dr < self.rows and 0 <= col + dc < self.columns:
                        self.reveal_cell(row + dr, col + dc)
        return False

    def flag_cell(self, row, col):
        if self.revealed_board[row][col] == ' ':
            self.revealed_board[row][col] = 'F'

    def play(self):
        print("Welcome to Minesweeper!")
        while True:
            self.display_board()
            row = int(input(f"Enter row (0-{self.rows - 1}): "))
            col = int(input(f"Enter column (0-{self.columns - 1}): "))
            action = input("Choose action (reveal/r or flag/f): ").lower()
            if action == 'reveal' or action == 'r':
                if self.reveal_cell(row, col):
                    print("Game over! You hit a mine.")
                    return
            elif action == 'flag' or action == 'f':
                self.flag_cell(row, col)
            if self.remaining_cells == 0:
                print("Congratulations! You won!")
                return
