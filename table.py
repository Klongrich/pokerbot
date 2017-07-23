from cardgen import deal

class table:
    __pot = 0
    __cards = []

    def getPot(self):
        return self.__pot

    def setPot(self, newPot):
        self.__pot = newPot

    def addPot(self, addPot):
        self.__pot += addPot

    def resetPot(self):
        self.__pot = 0;

    def getCards(self):
        return self.__cards

    def dealCards(self, turn, dealtCards):
        numCards = 0
        if turn == 'flop':
            numCards = 3
        elif (turn == 'turn') or (turn == 'river'):
            numCards = 1
        deal(self.__cards, numCards, dealtCards)