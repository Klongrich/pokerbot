import random

class deckOfCards:

    def __init__(self):
        self.unusedCards = [i for i in range(52)]
        self.usedCards = []
        random.shuffle(self.unusedCards)

    def getUsedCards(self):
        return self.usedCards

    def getunUsedCards(self):
        return self.unUsedCards

    def shuffle(self):
        del self.unusedCards[:]
        del self.usedCards[:]
        self.unusedCards = [i for i in range(52)]
        random.shuffle(self.unusedCards)

    def drawCard(self):
        for i in range(2):
            drawnCard = self.unusedCards.pop()
            self.usedCards.append(drawnCard)
            return drawnCard
