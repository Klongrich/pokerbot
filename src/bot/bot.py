

'''
- number of player;
- current hand;
- number of cards on the table;


-- Current Hand object
    - return suite
    - return cards on table
    - return cards in my hand

Bot.solve() key;

-2 = fold;
-1 = call;
0 = check;

> 0 = amount betting

As far as the algorithm is concered this i what I am thinking. We'll just take into account the probabailty
that other people have a better hand as well as the probabilty of having our hand. Basically how much are we risking vs what
is the expected result over thousands of games played.

Something like
(BP - Q) / B

B = the Decimal odds (2) - How much you can return from bet
P = probability of success (0.12)
Q = probability of failure (0.78)

((1)(0.12) - (0.78) / 1) = -0.66% (bot would fold)
((2)(0.40) - (0.54) / 2) = 13% (bot would bet 13 percent of it's chips)
....


'''

class bot:

    def __init__(self, current_hand):
        self.hand = current_hand
        self.chips = 714
        self.players = 5
        self.chips_in_pot = 100

    #Need amount of players, cards on table, and cards in my hand.
    def get_success_probabilty(self):
        return (0.714)

    def get_failure_probabilty(self):
        return (self.get_success_probabilty() - 1)

    #This needs to be accurate
    def get_probabilty(self):
        b = self.chips_in_pot / self.chips
        p = self.get_success_probabilty();
        q = self.get_failure_probabilty()
        return (((b * p) - q) / b)

    def bet_amount(self):
        return (self.chips * self.get_probabilty());

    #Need to now if I'm big blind, little blind, or neither;
    def solve_start(self):
        if self.current_hand.isTwopair() == 1:
            return (self.bet_amount())
        if self.current_hand.same_suit() == 1:
            return (self.bet_amount())
        else:
            return (-1)

    def solve(self):
        if len(self.cards_on_table) == 0:
            return (self.solve_start())

    def update_current_hand(self, updated_hand):
        self.current_hand = updated_hand



