# decisions and hand
import sys

from src.GUI.hand import *


class player:
    def __init__(self, name):
        self.myName = name.rstrip()
        self.myHand = current_hand()

# so the players and the bot should be able to take in a new hand
    def update_current_hand(self, hand):
        self.myHand = hand

    def get_my_hand(self):
        return self.myHand.get_cards()

    def get_my_hand_names(self):
        return self.myHand.get_names()

    def get_my_name(self):
        return self.myName

    '''
#  return -2 - x
    def mk_bet(self, myChips, comCards):
        print("---{0}'s Turn---".format(self.myName))
        print("Chips: {0}".format(myChips))
        print("Community cards:", comCards.getCardNames())
        # print("hand: {0}".format(self.myHand.getCardNames()))
        print("hand: {0}".format(self.get_my_hand()))
        print("Place your bet:")
        myBet = sys.stdin.readline()
        # add processing for actual words
        myBet = int(myBet)
        return myBet
    '''