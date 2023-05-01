#-------------------------------------------------------------------------------
import random

class SkatCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class SkatDeck:
    def __init__(self):
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for rank in ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
                self.cards.append(SkatCard(suit, rank))
        self.discard_pile = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def discard_card(self, card):
        self.discard_pile.append(card)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num_cards):
        for i in range(num_cards):
            card = deck.draw_card()
            self.hand.append(card)
            print(f"{self.name} draws {card}")

    def discard(self, deck):
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.hand):
            print(f"{i+1}: {card}")
        while True:
            try:
                choice = int(input(f"{self.name}, choose a card to discard: ")) - 1
                if choice < 0 or choice >= len(self.hand):
                    raise ValueError
                break
            except ValueError:
                print("Invalid choice, try again.")
        card = self.hand.pop(choice)
        deck.discard_card(card)
        print(f"{self.name} discards {card}")
        return card

def compare_cards(card1, card2):
    ranks = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    if ranks.index(card1.rank) < ranks.index(card2.rank):
        return 1
    elif ranks.index(card1.rank) > ranks.index(card2.rank):
        return 2
    else:
        return 0

deck = SkatDeck()
deck.shuffle()
player1 = Player("Player 1")
player2 = Player("Player 2")
winsplayer1 = 0
winsplayer2 = 0

# First round: draw 5 cards each
for player in [player1, player2]:
    player.draw(deck, 5)
    player_discard = player.discard(deck)
    if player == player1:
        player1_discard = player_discard
    else:
        player2_discard = player_discard

    # Compare discarded cards after each round
    if "player1_discard" in locals() and "player2_discard" in locals():
        print(f"Player 1's discard: {player1_discard}")
        print(f"Player 2's discard: {player2_discard}")
        winner = compare_cards(player1_discard, player2_discard)
        if winner == 1:
            winsplayer1 += 1
            print("Player 1 wins the round!")
        elif winner == 2:
            winsplayer2 += 1
            print("Player 2 wins the round!")
        else:
            print("It's a tie!")
        del player1_discard
        del player2_discard

# Subsequent rounds: draw 1 card each
for round_num in range(2, 5):
    print(f"Starting round {round_num}")
    for player in [player1, player2]:
        player.draw(deck, 1)
        player_discard = player.discard(deck)
        if player == player1:
            player1_discard = player_discard
        else:
            player2_discard = player_discard

        # Compare discarded cards after each round
        if "player1_discard" in locals() and "player2_discard" in locals():
            print(f"Player 1's discard: {player1_discard}")
            print(f"Player 2's discard: {player2_discard}")
            winner = compare_cards(player1_discard, player2_discard)
            if winner == 1:
                winsplayer1 += 1
                print("Player 1 wins the round!")
            elif winner == 2:
                winsplayer2 += 1
                print("Player 2 wins the round!")
            else:
                print("It's a tie!")
            del player1_discard
            del player2_discard

#Compare all the wins between player1 and player2
if winsplayer1 > winsplayer2:
    print("Player 1 wins the game!")
elif winsplayer2 > winsplayer1:
    print("Player 2 wins the game!")
else:
    print("It's a tie!")