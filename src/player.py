class player:

    def __init__(self):
        self.myChips = 100
        self.myHand = []

    def getChips(self):
        return self.myChips

    def setChips(self, chips):
        self.myChips = chips

    def addChips(self, chips):
        self.myChips += chips

    def bet(self, chips):
        self.myChips -= chips

    def addCard(self, card):
        self.myHand.append(card)

    def getHand(self):
        return self.myHand

    def delHand(self):
        del self.myHand[:]