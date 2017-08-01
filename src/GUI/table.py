import random

from src.GUI.hand import *


class table:

    def __init__(self, number_of_players):
        self.numPlayers = number_of_players

        # acts as the dealer button
        self.dealer = 0

        # dealing out cards for players and community cards
        self.deck = []
        self.playersHands = []
        self.comCards = current_hand()
        self.curPlayer = self.get_lit_blind()
        self.shuffle_deck()
        print("Current Deck:\n", self.get_deck())
        self.deal_player_hands()


        # keeping track of bets on the table as well as players chips
        # curBets hold the current bet so..
        # -2 = folded this round
        # -1 = called this round
        # 0 = checked this round
        # >0 = the amound bet (maybe make >= bigblind value
        self.bigBlindVal = 20
        self.litBlindVal = self.bigBlindVal / 2
        self.pot = 0            # change to accomodate side pots
        self.curBets = []
        self.playersChips = []
        for i in range(0, self.numPlayers):
            self.playersChips.append(1000)
            self.curBets.append(0)

    def get_deck(self):
        return self.deck

    def get_cur_player(self):
        return self.curPlayer

    def set_cur_player(self, next_player):
        self.curPlayer = next_player

    def get_pot(self):
        return self.pot

    def get_com_cards(self):
        return self.comCards

    def get_dealer(self):
        return self.dealer

    def get_lit_blind(self):
        return self.get_next_player(self.dealer)

    def get_big_blind(self):
        return self.get_next_player(self.get_lit_blind())

    def get_num_players(self):
        return self.numPlayers

    def get_player_chips(self, p):
        return self.playersChips[p]

    def get_next_player(self, p):
        if p == self.numPlayers - 1:
            return 0
        else:
            return p + 1

    def get_prev_player(self, p):
        if p == 0:
            return self.numPlayers - 1
        else:
            return p - 1

# dealing cards
    def shuffle_deck(self):
        del self.deck[:]
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def deal_player_hands(self):
        for i in range(0, self.numPlayers):
            self.playersHands.append(current_hand())
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



    '''
# betting functions
# add something for when players only have 10 chips and bigblind is 20
    def is_pot_right(self):
        return False

    def is_in_hand(self, p):
        if self.curBets[p] == -2:
            return False
        else:
            return True


    # finds the last amound bet. Will return a value >= 0
    def get_prev_bet(self, p):
        prevPlayer = self.get_prev_player(p)
        if self.curBets[prevPlayer] == -2:
            return self.get_prev_bet(prevPlayer)
        else:
            return self.curBets[prevPlayer]

    # takes the player # and amount bet
    # returns 1 if it is a valid bet and 0 if it is not
    def tk_bet(self, p, bet):
        prevBet = self.get_prev_bet(p)
        # fold
        if bet == -2:
            self.curBets[p] = bet
            return 1
        # call
        elif bet == -1:
            self.curBets[p] = prevBet
            return 1
        # check
        elif (bet == 0) and (prevBet == 0):
            self.curBets[p] = prevBet
            return 1
        else:
            return 0



    '''

    def reset_table(self, winner):
        self.dealer = self.get_next_player(self.dealer)
        self.curPlayer = self.get_lit_blind()

        self.comCards = current_hand()
        self.shuffle_deck()
        print("Current Deck:\n", self.get_deck())
        self.deal_player_hands()

        self.playersChips[winner] += self.pot
        self.pot = 0





