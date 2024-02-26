from hangman import hangman
from noughts_and_crosses import noughts_and_crosses
from battleship import Game
from blackjack import BlackjackGame
from connect_four import Connect4Game
from minesweeper import MinesweeperGame

def display_menu():
    print("\n=====================")
    print("      Main Menu      ")
    print("=====================")
    print(" 1. Hangman")
    print(" 2. Noughts & Crosses")
    print(" 3. Battleships")
    print(" 4. Blackjack")
    print(" 5. Connect 4")
    print(" 6. Minesweeper")
    print(" 7. Quit")
    print("=====================")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nYou selected Hangman\n")
            hangman()
        elif choice == "2":
            print("\nYou selected Noughts & Crosses\n")
            noughts_and_crosses()
        elif choice == "3":
            print("\nYou selected Battleships\n")
            battleship_game = Game("Player 1", "Player 2")
            battleship_game.play()
        elif choice == "4":
            print("\nYou selected Blackjack\n")
            blackjack_game = BlackjackGame()
            blackjack_game.play()
        elif choice == "5":
            print("\nYou selected Connect 4\n")
            connect4_game = Connect4Game()
            connect4_game.play()
        elif choice == "6":
            print("\nYou selected Minesweeper\n")
            minesweeper_game = MinesweeperGame()
            minesweeper_game.play()
        elif choice == "7":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
