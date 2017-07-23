from cardgen import deal

class player:

    def __init__(self, chips):
        self.__chips = chips
        self.__hand = []

    def getChips(self):
        return self.__chips

    def setChips(self, chips):
        self.__chips = chips

    def addChips(self, chips):
        self.__chips += chips

    def bet(self, chips):
        self.__chips -= chips

    def newHand(self, dealtCards):
        deal(self.__hand, 2, dealtCards)

    def getHand(self):
        return self.__hand

    def delHand(self):
        del self.__hand[:]