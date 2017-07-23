import random

# pass in player or table "hand", number of cards that needs to be generated
# and master list of cards used in the current deck
def deal(hand, numCards, dealtCards):
    for i in range(0, numCards):
        while True:
            c = random.randint(0, 51)
            if c not in dealtCards:
                hand.append(c)
                dealtCards.append(c)
                break
