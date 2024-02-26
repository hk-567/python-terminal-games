import random
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank,suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal(self): 
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards =[]
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        value = 0 
        num_aces=0
        for card in self.cards:
            if card.rank.isdigit():
                value += int(card.rank)
            elif card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                num_aces += 1
                value += 11
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value
    def __str__(self):
        return ', '.join(str(card)for card in self.cards)
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_initial_cards(self):
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def player_turn(self):
        while True:
            print("Your hand:", self.player_hand)
            print("Your hand value:", self.player_hand.calculate_value())
            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                self.player_hand.add_card(self.deck.deal())
                if self.player_hand.calculate_value() > 21:
                    print("Bust! You lose.")
                    return False
            elif choice == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        return True

    def dealer_turn(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())
        print("Dealer's hand:", self.dealer_hand)
        print("Dealer's hand value:", self.dealer_hand.calculate_value())

    def determine_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()
        if player_value > 21:
            print("Player busts! Dealer wins.")
        elif dealer_value > 21 or player_value > dealer_value:
            print("Player wins!")
        elif player_value == dealer_value:
            print("It's a tie!")
        else:
            print("Dealer wins.")

    def play(self):
        print("Welcome to Blackjack!")
        while True:
            self.deck = Deck()  # Reset the deck
            self.player_hand = Hand()
            self.dealer_hand = Hand()
            self.deal_initial_cards()
            if not self.player_turn():
                break
            self.dealer_turn()
            self.determine_winner()
            again = input("Do you want to play again? (y/n): ").lower()
            if again != 'y':
                break

