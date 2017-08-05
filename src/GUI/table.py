'''

'''
import random
from src.GUI.human import *


class table:

    bet_amount = 0
    pot = 15000

    def __init__(self, number_of_players):
        self.numPlayers = number_of_players

        self.dealer = 0

        # dealing out cards for players and community cards
        self.deck = []
        self.playersHands = []
        self.comCards = player("foo")
        self.shuffle_deck()
        self.deal_player_hands()



    def get_deck(self):
        return self.deck

    def get_pot(self):
        return self.pot

    def get_com_cards(self):
        return self.comCards

    def get_dealer(self):
        return self.dealer


# dealing cards
    def shuffle_deck(self):
        del self.deck[:]
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def deal_player_hands(self):
        for i in range(0, self.numPlayers):
            self.playersHands.append(player("foo"))
        for i in range(0, 2):
            for j in range(0, self.numPlayers):
                self.playersHands[j].add_card(self.draw_card())

    def get_next_hand(self):
        nextHand = self.playersHands.pop(0)
        return nextHand

    def deal_com_cards(self, turn):
        numCards = 0
        if turn == 'flop':
            numCards = 3
        elif (turn == 'turn') or (turn == 'river'):
            numCards = 1
        for i in range(0, numCards):
            self.comCards.add_card(self.draw_card())


    def reset_table(self, winner):

        self.comCards = player("foo")
        self.shuffle_deck()
        self.deal_player_hands()






