class Player:
    def __init__(self, name):
        self.name = name
        self.ship_grid = [[' ']*10 for _ in range(10)]
        self.attack_grid = [[' ']*10 for _ in range(10)]

    def place_ship(self, ship, row, col, orientation):
        if orientation == "horizontal":
            if col + ship.size > 10:
                print("Ship placement out of bounds.")
                return False
            for i in range(ship.size):
                if self.ship_grid[row][col+i] != ' ':
                    print("Overlap with another ship.")
                    return False
            for i in range(ship.size):
                self.ship_grid[row][col + i] = ship.symbol
        elif orientation == "vertical":
            if row + ship.size > 10:
                print("Ship placement out of bounds.")
                return False
            for i in range(ship.size):
                if self.ship_grid[row + i][col] != ' ':
                    print("Overlap with another ship.")
                    return False
            for i in range(ship.size):
                self.ship_grid[row + i][col] = ship.symbol
        else:
            print("Invalid orientation.")
            return False
        print(f"{ship.name} placed successfully.")
        self.print_ship_grid()  # Print ship grid after ship placement
        return True


    def make_attack(self, row, col, opponent):
        if row < 0 or row >= 10 or col < 0 or col >= 10:
            print("Attack out of bounds")
            return False
        if self.attack_grid[row][col] != ' ':
            print("You've already attacked this position.")
            return False
        self.attack_grid[row][col] = 'X'
        if opponent.ship_grid[row][col] != ' ':
            print("Hit!")
            opponent.ship_grid[row][col] = 'X'
            return True
        else:
            print("Miss!")
            return False

    def print_ship_grid(self):
        print(f"Ship Grid for {self.name}:")
        print("   0 1 2 3 4 5 6 7 8 9")
        for i, row in enumerate(self.ship_grid):
            print(f"{i} {' '.join(row)}")

    def print_attack_grid(self):
        print(f"Attack Grid for {self.name}:")
        print("   0 1 2 3 4 5 6 7 8 9")
        for i, row in enumerate(self.attack_grid):
            print(f"{i} {' '.join(row)}")


class Ship:
    def __init__(self, name, size, symbol):
        self.name = name
        self.size = size
        self.symbol = symbol
        self.hits = 0

    def is_sunk(self):
        return self.hits == self.size

    def hit(self):
        self.hits += 1


class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.current_player = self.player1
        self.other_player = self.player2

    def switch_turn(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def play(self):
        print("Battleship game starts!")
        for player in [self.player1, self.player2]:
            print(f"{player.name}, place your ships:")
            for ship_name, ship_size, ship_symbol in [("Destroyer", 2, "D"), ("Submarine", 3, "S"), ("Battleship", 4, "B"), ("Aircraft Carrier", 5, "A")]:
                while True:
                    print(f"Placing {ship_name} (size {ship_size}):")
                    try:
                        row = int(input("Enter row (0-9): "))
                        col = int(input("Enter column (0-9): "))
                        orientation = input("Enter orientation (horizontal or vertical): ").lower()
                        if orientation not in ["horizontal", "vertical"]:
                            raise ValueError("Invalid orientation. Must be 'horizontal' or 'vertical'.")
                        if player.place_ship(Ship(ship_name, ship_size, ship_symbol), row, col, orientation):
                            break
                    except ValueError as e:
                        print(f"Error: {e}")

        print("\nBattleship game setup complete!\n")

        while True:
            print(f"It's {self.current_player.name}'s turn")
            self.current_player.print_attack_grid()
            print("\n")
            while True:
                try:
                    row = int(input("Enter row to attack (0-9): "))
                    if 0 <= row <= 9:
                        break
                    else:
                        print("Invalid input, row must be between 0 and 9.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            while True:
                try:
                    col = int(input("Enter column to attack (0-9): "))
                    if 0 <= col <= 9:
                        break
                    else:
                        print("Invalid input. Column must be between 0 and 9.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            hit = self.current_player.make_attack(row, col, self.other_player)

            if hit:
                print("You get another turn")
            else:
                print("Turn ends")

            if all(all(cell == 'X' for cell in row) for row in self.other_player.ship_grid):
                print(f"{self.current_player.name} wins!")
                break

            if not hit:
                self.switch_turn()



