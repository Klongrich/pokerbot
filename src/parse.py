#function takes in any number of cards and compares them to all 10 possible outcomes
#starting with the lowerst probability (royal flush) to the highest probability (high card)

def parse_hands(*args):
    usable_cards = args

    #create suit stripped versions of the below code if possible
    suit_stripped = []
    for card in usable_cards:
        suit_stripped.append(card % 13)

    # check for the best hands first
    #move del matches before return statements
    # check royal flush
    for i in range(0,4):
        royal_flush = [8 + (i * 13),
                       9 + (i * 13),
                       10 + (i * 13),
                       11 + (i * 13),
                       12 + (i * 13)]

        matches = list(set(usable_cards).intersection(royal_flush))
        if len(matches) == 5:
            return 9
        del matches[:]



    # check straight flush
    for i in range(0, 4):
        for j in range(0, 9):
            if j == 8:
                straight_flush = [0 + (i * 13),
                                  1 + (i * 13),
                                  2 + (i * 13),
                                  3 + (i * 13),
                                  12 + (i * 13)]
            else:
                straight_flush = [0 + j + (i * 13),
                                  1 + j + (i * 13),
                                  2 + j + (i * 13),
                                  3 + j + (i * 13),
                                  4 + j + (i * 13)]
            matches = list(set(usable_cards).intersection(straight_flush))
            if len(matches) == 5:
                return 8
            del matches[:]

    # check 4 of a kind
    for i in range(0, 13):
        four_kind = [0 + i, 13 + i, 26 + i, 39 + i]
        matches = list(set(usable_cards).intersection(four_kind))
        if len(matches) == 4:
            return 7
        del matches[:]

    # check full house
    # need to make look better + test
    count = 0
    for i in range(0, 13):
        pair = [0 + i, 13 + i, 26 + i, 39 + i]
        matches = list(set(usable_cards).intersection(pair))
        if len(matches) == 2:
            count +=1
        elif len(matches) == 3:
            count +=3
        elif count >= 4:
            return 1
        del matches[:]

    # check flush
    for i in range(0, 4):
        flush = [0 + (i * 13), 1 + (i * 13), 1 + (i * 13), 3 + (i * 13),
                 4 + (i * 13), 5 + (i * 13), 6 + (i * 13), 7 + (i * 13),
                 8 + (i * 13), 9 + (i * 13), 10 + (i * 13), 11 + (i * 13),
                 12 + (i * 13)]
        matches = list(set(usable_cards).intersection(flush))
        if len(matches) == 5:
            return 5
        del matches[:]

    # check straight
    for i in range(0, 9):
        if i == 8:
            straight = [0, 1, 2, 3, 12]
        else:
            straight = [0 + i, 1 + i, 2 + i, 3 + i, 4 + i]
        matches = list(set(suit_stripped).intersection(straight))
        if len(matches) == 5:
            return 4
        del matches[:]


    # check 3 of a kind
    for i in range(0, 13):
        three_kind = [0 + i, 13 + i, 26 + i, 39 + i]
        matches = list(set(usable_cards).intersection(three_kind))
        if len(matches) == 3:
            return 3
        del matches[:]

    # check two pair
    num_of_pairs = 0
    for i in range(0, 13):
        two_pair = [0 + i, 13 + i, 26 + i, 39 + i]
        matches = list(set(usable_cards).intersection(two_pair))
        if len(matches) == 2:
            num_of_pairs += 1
        if num_of_pairs ==2:
            return 2
        del matches[:]

    # check pair
    for i in range(0, 13):
        pair = [0 + i, 13 + i, 26 + i, 39 + i]
        matches = list(set(usable_cards).intersection(pair))
        if len(matches) == 2:
            return 1
        del matches[:]

    # check high card
    # with this system last option will be high card
    # since it apparently doesn't matter what high card it is
    return 0