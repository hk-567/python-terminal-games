def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def noughts_and_crosses():
    board = [[' ']*3 for _ in range(3)]
    player = 'X'
    turns = 0

    print("Let's play Noughts & Crosses!")
    print_board(board)

    while turns < 9:
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                if row not in [0,1,2]:
                    raise ValueError
                col = int(input("Enter column (0, 1, or 2): "))
                if col not in [0,1,2]:
                    raise ValueError   
                if board[row][col] != ' ':
                    print("That spot is already taken. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")
        board[row][col] = player
        turns += 1
        print_board(board)

        if check_winner(board):
            print(f"Player {player} wins!")
            return

        player = 'O' if player == 'X' else 'X'

    print("It's a draw!")

