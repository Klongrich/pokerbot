import sys
from parse import *
from player import *
from table import *

'''
# ---main---
# keeps track of cards in the deck used
dealtCards = []

print("How many Players?")
players = sys.stdin.readline()
players = int(players)
deal_players(players, dealtCards)

# create dictionary to hold players cards
# Player 1 will be bot always
# can cycle through which player starts first in another loop
dct = {}
for i in range(0, players):
    dct['player_%s' % (i + 1)] = [dealtCards[i], dealtCards[i + players]]

print(parse_hands(dct['player_1'][0], dct['player_1'][1]))

deal_flop(dealtCards)

print(parse_hands(dct['player_1'][0], dct['player_1'][1],
                  dealtCards[(players * 2)], dealtCards[(players * 2) + 1],
                  dealtCards[(players * 2) + 2]))

deal_turn(dealtCards)

print(parse_hands(dct['player_1'][0], dct['player_1'][1],
                  dealtCards[(players * 2)], dealtCards[(players * 2) + 1],
                  dealtCards[(players * 2) + 2], dealtCards[(players * 2) + 3]))

deal_river(dealtCards)

print(parse_hands(dct['player_1'][0], dct['player_1'][1],
                  dealtCards[(players * 2)], dealtCards[(players * 2) + 1], dealtCards[(players * 2) + 2],
                  dealtCards[(players * 2) + 3], dealtCards[(players * 2) + 4]))

print(dealtCards)
print(dct)
'''
# ---main---
# each player can have two cards, the table can have 0-5 cards
# chips = money
chips = 100
dealtCards = []
players = []

# can just remove a player when out of chips

print("How many Players?")
numOfPlayers = int(sys.stdin.readline())

for i in range(0, numOfPlayers):
    players.append(player(chips))

# game loop
# should be for loops for betting and dealing cards right?
# so
while True:

    for i in range(0, numOfPlayers):
        players[i].newHand(dealtCards)
        print(players[0].getHand())
        print(players[1].getHand())
        print(dealtCards)

    newTable = table()
    
    newTable.dealCards('flop', dealtCards)
    
    newTable.dealCards('turn', dealtCards)
    
    newTable.dealCards('river', dealtCards)





    print("Do you want to play again?")
    play_again = sys.stdin.readline()
    play_again.lower()
    if play_again[0] == 'n':
        break

    # add handling for when players out of chips
    del dealtCards[:]


# i want it to look like this
'''

'''