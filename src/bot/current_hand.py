'''

Suites

0 = spades;
1 = clubs;
2 = hearts;
3 = diamonds;

self.card_suites = [first card in myhand, second card in my hand, first card on table, etc ..]


'''

class current_hand:

    def __init__(self):
        self.myhand = [2, 3];
        self.cards_on_table = [23, 24, 17, 29, 11];
        self.card_suites = [1, 0, 2, 3, 3, 2, 0];

    def get_myhand(self):
        return (self.myhand);

    def get_cards_on_table (self):
        return (self.cards_on_table)

    def get_card_suites(self):
        return (self.get_card_suites());