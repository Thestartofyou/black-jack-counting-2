'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
import random

# Initialize the deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# Initialize the running count and the number of decks
running_count = 0
num_decks = 4

# Function to deal a card from the deck
def deal_card():
    global deck
    card = random.choice(deck)
    deck.remove(card)
    return card

# Function to calculate the true count
def true_count():
    global running_count
    global num_decks
    remaining_cards = len(deck)
    decks_remaining = remaining_cards / (52 * num_decks)
    return running_count / decks_remaining

# Play a round of blackjack
def play_blackjack():
    global running_count
    player_total = 0
    dealer_total = 0

    # Deal the cards
    player_total += deal_card()
    dealer_total += deal_card()
    player_total += deal_card()
    dealer_total += deal_card()

    # Player's turn
    while player_total < 21:
        if true_count() >= 1:
            # If the true count is 1 or higher, the player should bet more
            bet = 10
        else:
            bet = 5

        # Ask the player if they want to hit or stand
        action = input("Do you want to hit or stand? ")
        if action == "hit":
            player_total += deal_card()
        else:
            break

    # Dealer's turn
    while dealer_total < 17:
        dealer_total += deal_card()

    # Determine the winner
    if player_total > 21:
        print("Player busts! Dealer wins.")
        running_count -= 1
    elif dealer_total > 21:
        print("Dealer busts! Player wins.")
        running_count += 1
    elif player_total > dealer_total:
        print("Player wins!")
        running_count += 1
    elif player_total < dealer_total:
        print("Dealer wins.")
        running_count -= 1
    else:
        print("Push.")

    print("Running count:", running_count)

# Play multiple rounds of blackjack
while True:
    play_blackjack()
