class Connect4Game:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.columns * 2 - 1))

    def is_valid_move(self, column):
        return 0 <= column < self.columns and self.board[0][column] == ' '

    def drop_token(self, column):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return row

    def check_winner(self, row, column):
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]  # vertical, horizontal, diagonal (right), diagonal (left)
        for dr, dc in directions:
            count = 1
            for step in range(1, 4):
                r, c = row + step * dr, column + step * dc
                if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            for step in range(1, 4):
                r, c = row - step * dr, column - step * dc
                if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == self.current_player:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False

    def play(self):
        print("Welcome to Connect 4!")
        while True:
            self.display_board()
            column = int(input(f"Player {self.current_player}, choose a column (0-{self.columns - 1}): "))
            if self.is_valid_move(column):
                row = self.drop_token(column)
                if self.check_winner(row, column):
                    print(f"Player {self.current_player} wins!")
                    break
                if all(self.board[0][i] != ' ' for i in range(self.columns)):
                    print("It's a draw!")
                    break
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print("Invalid move. Please choose an empty column.")
