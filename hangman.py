def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_"
    return display

def hangman():
    print("This is a two-player game. Player 1 will select a word for Player 2 to guess.")
    
    while True:
        word_to_guess = input("Player 1, enter a word you want Player 2 to guess: ").lower()
        if not word_to_guess.isalpha():
            print("Invalid input. Please enter a word containing only letters.")
            continue
        break    
    
    
    
    
    guessed_letters = set()
    incorrect_guesses = 6

    print("\nLet's play Hangman")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_guesses > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else: 
            print("Incorrect")
            incorrect_guesses -= 1
        
        print(display_word(word_to_guess, guessed_letters))
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            return
    print("Sorry, you ran out of guesses. The word was:", word_to_guess)