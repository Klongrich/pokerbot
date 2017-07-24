from deckOfCards import deckOfCards

class table:

    def __init__(self):
        self.pot = 0
        self.comCards = []

    def getPot(self):
        return self.pot

    def setPot(self, newPot):
        self.pot = newPot

    def addPot(self, addPot):
        self.pot += addPot

    def resetPot(self):
        self.pot = 0;

    def getCards(self):
        return self.comCards

    def dealCards(self, turn, deck):
        numCards = 0
        if turn == 'flop':
            numCards = 3
        elif (turn == 'turn') or (turn == 'river'):
            numCards = 1
        for i in range(0, numCards):
            drawnCard = deck.drawCard()
            self.comCards.append(drawnCard)

    def resetTable(self):
        self.pot = 0
        del self.comCards[:]