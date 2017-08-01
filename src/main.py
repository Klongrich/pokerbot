from src.GUI.player import *
from src.GUI.table import *

'''
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
'''

# ---main---
players = []

print("How many human Players?")
# plus one for the bot once its added
myTable = table(int(sys.stdin.readline()))

for i in range(0, myTable.numPlayers):
    print("Enter Players Name:")
    name = sys.stdin.readline()
    players.append(player(name))

# terminator = bot(hand())
# players.append(terminator)


# game loop
while len(players) != 1:
    numPlayers = myTable.get_num_players()
    print("Current Deck:\n", myTable.get_deck())


    # deal out hands to players starting with the little blind then to the left around the table
    # players and bots need to have a method .update_current_hand(current_hand()) that accepts a new hand object
    for j in range(0, numPlayers):
        curPlayer = myTable.get_cur_player()
        players[curPlayer].update_current_hand(myTable.get_next_hand())

        print("\n", players[curPlayer].get_my_name(), "'s hand:")
        print("Raw Card Values:", players[curPlayer].get_my_hand())
        print("Card Suites:", players[curPlayer].myHand.get_suites())
        print("Card Values:", players[curPlayer].myHand.get_values())
        print("Actual Card Names:", players[curPlayer].get_my_hand_names())

        myTable.set_cur_player(myTable.get_next_player(curPlayer))

    myTable.deal_com_cards('flop')
    print("Current Deck:\n", myTable.get_deck())
    print("Community Cards:\n", myTable.get_com_cards().get_cards())

    myTable.deal_com_cards('turn')
    print("Current Deck:\n", myTable.get_deck())
    print("Community Cards:\n", myTable.get_com_cards().get_cards())

    myTable.deal_com_cards('river')
    print("Current Deck:\n", myTable.get_deck())
    print("Community Cards:\n", myTable.get_com_cards().get_cards())

    sys.stdin.readline()



# reset table first to change the chips, then if pChips = 0, remove them from the game
    myTable.reset_table(0)
    for j in range(0, numPlayers):
        if myTable.get_player_chips(j) == 0:
            print(players[j].getName(), "is out of the game!")
            players.pop(j)
