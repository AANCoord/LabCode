# shuffle(list) : returns a list of shuffle values. [1,2,4,5] -> [5,1,2,4]
from random import shuffle

# sleep(3): delays the program by 3 seconds
from time import sleep

SUITS = ['♠️','♥️','♣️','♦️']
VALUE_KEY = {'A': 14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 ,'10':10, 'J':11, 'Q':12 ,'K':13, '0':0}

class Card:

    def __init__(self, suit, value):
        """Initializier for a Card object that contains a suit and a value."""

        self.suit = suit
        self.val = value
    
    def __str__(self):
        """Returns the string representation of a card."""

        return f"{self.val}{self.suit}"
    
    def value(self):
        """Return the value that is on the card."""

        return self.val

class Deck:

    def __init__(self):
        """Initializer for a DECK object that holds each card."""

        self.cards = []
        self.shuffle_cards()
    
    def hit(self):
        """Removes the card from the top of the deck and returns the value."""

        if self.cards:
            return self.cards.pop()
        else:
            self.shuffle_cards()
            return self.cards.pop()
    
    def shuffle_cards(self):
        """Creates and shuffle the cards in a deck. If playing WAR leave the second black of code commented since
        blackjack uses 8 deck of cards. Leave the first deck uncommented if you are playing war."""

        # UNCOMMENT this code if you are playing War
        self.cards = []
        for suit in SUITS:
            for value in VALUE_KEY.keys():
                self.cards.append(Card(suit, value))
        
        shuffle(self.cards)
    
    def empty(self):
        """Returns True or False depending on if the deck is empty."""

        return True if self.deck else False
        

def clear_screen():
    """Clear the contents of the console."""
    sleep(4)
    for i in range(100):
        print()

def print_hand(cards):
    """
    Prints each card in the list of cards.
        Keyword arguments:
        cards     --  A list of card objects
    """
    for card in cards:
        print(card)

def deal_cards(players):

    for i in range(26):
        for j in range(1, 3):
            players[j].append(deck.hit())
    
    return players

def no_winner(players):

    i = 1
    for player_hand in players.values():
        print(f"Player {i} has {len(player_hand)} cards.")
        if len(player_hand) == 52:
            return False
        i +=1
    
    return True

def declare_winner(players_hand):

    if len(players_hand[1]) > len(players_hand[2]):
        return "Congrats Player 1, you won!"
    else:
        return "Congrats Player 2, you won!"


def draw(p1_card, p2_card, players_hand):

    cards_to_add = [p1_card, p2_card]
    if len(players_hand[1]) != 0:
        p1_next = players_hand[1].pop(0)
    else:
        p1_next = Card('0','0')
    if len(players_hand[2]) != 0:
        p2_next = players_hand[2].pop(0)
    else:
        p2_next = Card('0','0')
    print(p1_next)
    print(p2_next)
    while VALUE_KEY[p1_next.value()] == VALUE_KEY[p2_next.value()]:
        cards_to_add += [p1_next, p2_next]
        p1_next = players_hand[1].pop(0)
        p2_next = players_hand[2].pop(0)
        print(p1_next)
        print(p2_next)
        if VALUE_KEY[p1_next.value()] > VALUE_KEY[p2_next.value()]:
            print("PLayer 1 has a higher value")
            players_hand[1] += (cards_to_add + [p1_next, p2_next])
        elif VALUE_KEY[p2_next.value()] > VALUE_KEY[p1_next.value()]:
            print("PLayer 2 has a higher value")
            players_hand[2] += (cards_to_add + [p1_next, p2_next])
    
    return players_hand

# {1: [c1, c2], 2: [c4, c3]}
# def play_war(players_hand):
def play_war(players_hand):
    while no_winner(players_hand):
        sleep(.5)
        p1_card = players_hand[1].pop(0)
        p2_card = players_hand[2].pop(0)
        print(p1_card)
        print(p2_card)

        if VALUE_KEY[p1_card.value()] > VALUE_KEY[p2_card.value()]:
            print("Player 1 Had a higher value")
            players_hand[1] += [p1_card, p2_card]
        elif VALUE_KEY[p2_card.value()] > VALUE_KEY[p1_card.value()]:
            print("PLayer 2 has a higher value")
            players_hand[2] += [p1_card, p2_card]
        else:
            players_hand = draw(p1_card, p2_card, players_hand)
    
    print(declare_winner(players_hand))


        


def war():

    # {player_name : hand of cards}
    players = {1:[], 2: []}
    # print(players[1])
    # print(players[2])

    players = deal_cards(players)
    play_war(players)


    
##################DO NOT EDIT BELOW THIS LINE################
def main():
    """The main function that starts the game of blackjack"""
    global deck
    deck = Deck()

    war()

# This invokes the main function.  It is always included in our
# python programs. 
if __name__ == "__main__":
    main()