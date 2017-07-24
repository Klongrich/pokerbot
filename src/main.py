import sys
from player import *
from table import *
from deckOfCards import *

'''
the cards work like this right now
spades  clubs   hearts  diamonds
0       13      26      39          two
1       14      27      40          three
2       15      28      41          four
3       16      29      42          five
4       17      30      43          six
5       18      31      44          seven 
6       19      32      45          eight
7       20      33      46          nine
8       21      34      47          ten
9       22      35      48          jack
10      23      36      49          queen
11      24      37      50          king
12      25      38      51          ace

it made sense when doing the parsing to make it this way
so i can change it to a list of the actual strings if that makes it easier for you
ex ['two of spades', 'three of spades', ....]
or i could just have a function for it that would return the string value of
the corresponding number
ex. getValue(0) = 'two of spades'


also now a deck of cards is a class that contains both a list of used cards
and unused cards. 

so now parse_hand would take in the players cards + the community cards
'''



# ---main---

players = []
deck = deckOfCards()


print("How many Players?")
numOfPlayers = int(sys.stdin.readline())

for i in range(0, numOfPlayers):
    players.append(player())

# game loop

while True:
    # "dealer" is player0 then player1... then back to player0 shifts one to the left everytime
    # little blind is to the left of the dealer, big blind is to the left of little blind
    for dealer in range(0, numOfPlayers):
        # deal of cards one by one starting with the dealer
        curPlayer = dealer
        for i in range(0, 2):
            for j in range(0, numOfPlayers):
                drawnCard = deck.drawCard()
                players[curPlayer].addCard(drawnCard)
                if curPlayer < (numOfPlayers - 1):
                    curPlayer += 1
                else:
                    curPlayer = 0

        # show current hands
        print("current player hands")
        for i in range(0, len(players)):
            print(players[i].getHand())

        myTable = table()

        myTable.dealCards('flop', deck)
        print("current community cards")
        print(myTable.getCards())

        myTable.dealCards('turn', deck)
        print("current community cards")
        print(myTable.getCards())

        myTable.dealCards('river', deck)
        print("current community cards")
        print(myTable.getCards())


        # delete players hands, community cards, and shuffle the deck
        for i in range(0, len(players)):
            players[i].delHand()

        myTable.resetTable()
        deck.shuffle()

        # allow for bets starting with little blind

        # for testing
        print("Do you want to play again?")
        play_again = sys.stdin.readline()
        play_again.lower()
        if play_again[0] == 'n':
            break

    # for testing
    print("Do you want to play again?")
    play_again = sys.stdin.readline()
    play_again.lower()
    if play_again[0] == 'n':
        break

    # add handling for when players out of chips
