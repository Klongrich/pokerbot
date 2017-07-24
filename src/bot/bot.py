'''
- number of player;
- current hand;
- number of cards on the table;


-- Current Hand object
    - return suite
    - return cards on table
    - return cards in my hand


'''


class bot:

    def __init__(self, current_hand):
        self.current_hand = current_hand.get_myhand()
        self.cards_on_table = current_hand.get_cards_on_table()
        self.suites = current_hand.get_card_suites()
        self.chips = 714
        self.players = 5;

    def set_number_of_player(self, players):
        self.number_of_players = players;

    def set_current_hand(self, hand):
        self.current_hand = hand;

    def set_cards_on_table(self, cards):
        self.cards_on_table = cards

    def set_suites(self, suites):
        self.suites = suites


