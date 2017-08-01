
class current_hand:

    def __init__(self):
        self.myCards = []

# adds card to the hand (so you can deal one card at a time like real texas holdem)
    def add_card(self, card):
        self.myCards.append(card)

# returns list 0 - 51
    def get_cards(self):
        return self.myCards

# returns a list 0 - 3 (spade, club, heart, diamond)
    def get_suites(self):
        suites = []
        for i in range(0, len(self.myCards)):
            suites.append(self.myCards[i] // 13)
        return suites

# returns a list 0 - 12 (two - ace)
    def get_values(self):
        values = []
        for i in range(0, len(self.myCards)):
            suite = self.myCards[i] // 13
            values.append(self.myCards[i] - suite * 13)
        return values

# returns a list of strings like [Two of hearts, Three of Hearts]
    def get_names(self):
        values = self.get_values()
        suites = self.get_suites()
        name = []
        for i in range(0, len(self.myCards)):
            if values[i] == 0:
                name.append("Two of ")
            elif values[i] == 1:
                name.append("Three of ")
            elif values[i] == 2:
                name.append("Four of ")
            elif values[i] == 3:
                name.append("Five of ")
            elif values[i] == 4:
                name.append("Six of ")
            elif values[i] == 5:
                name.append("Seven of ")
            elif values[i] == 6:
                name.append("Eight of ")
            elif values[i] == 7:
                name.append("Nine of ")
            elif values[i] == 8:
                name.append("Ten of ")
            elif values[i] == 9:
                name.append("Jack of ")
            elif values[i] == 10:
                name.append("Queen of ")
            elif values[i] == 11:
                name.append("King of ")
            elif values[i] == 12:
                name.append("Ace of ")

            if suites[i] == 0:
                name[i] += "Spades"
            elif suites[i] == 1:
                name[i] += "Clubs"
            elif suites[i] == 2:
                name[i] += "Hearts"
            elif suites[i] == 3:
                name[i] += "Diamonds"
        return name

    def isTwopair(self):
        return (1)

    def same_suit(self):
        return (1)