'''
Documenation ohh boy....

Turn Variable Key:
0 = no cards delt
1 = 2 cards delt
2 = flop
3 = turn
4 = river

I want to add in some fancy stuff latter possible with graphics and anamation. Stuff like chips sliding around the table and what not.
But for now I think just a functional game would be good. Mainly because I need one in order to debug / play the Bot I am trying to create

'''

from src.GUI.bet_window import *
from src.GUI.human import player
from src.GUI.table import table

class GUI:

    def __init__(self, master):
        self.frame = Frame(master, background="dark green", highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
        self.frame.pack()

        self.bet_amount = 0
        self.turn = 0

        ''' Here is where the table cards are shown'''
        self.cardOne = Label(self.frame, image=ace_of_spades)
        self.cardTwo = Label(self.frame, image=two_of_spades)
        self.cardThree = Label(self.frame, image=three_of_spades)
        self.cardFour = Label(self.frame, image=four_of_spades)
        self.cardFive = Label(self.frame, image=five_of_spades)

        self.cardOne.grid(row=1, column=0, sticky=E)
        self.cardTwo.grid(row=1, column=1)
        self.cardThree.grid(row=1, column=2)
        self.cardFour.grid(row=1, column=3)
        self.cardFive.grid(row=1, column=4)

        ''' All the buttons for doing stuff'''
        self.betButton = Button(self.frame, text="Bet", width=10, command=self.bet)
        self.betButton.grid(row=3, column=0, pady=80)

        self.checkButton = Button(self.frame, text="check", width=10, command=self.check)
        self.checkButton.grid(row=3, column=1)

        self.foldButton = Button(self.frame, text="Fold", width=10, command=self.fold)
        self.foldButton.grid(row=3, column=2)

        self.callButton = Button(self.frame, text="Call", width=10, command=self.call)
        self.callButton.grid(row=3, column=3)

        self.raiseButton = Button(self.frame, text="Raise", width=10, command=self.Raise)
        self.raiseButton.grid(row=3, column=4)

        self.dealButton = Button(self.frame, text="Deal", width=10, command=self.deal)
        self.dealButton.grid(row=4, column=4)

        ''' Where your cards are shown '''
        self.player_cardone = Label(self.frame, image=player_CardOne)
        self.player_cardtwo = Label(self.frame, image=player_CardTwo)

        self.player_cardone.grid(row=4, column=0)
        self.player_cardtwo.grid(row=4, column=1)

        self.set_labels()


    def set_labels(self):
        chips = "Chips: " + str(Player.get_chips())
        bet = "Bet: " + str(self.bet_amount)
        pot = "Pot: " + str(Table.get_pot())

        self.chipsLabel = Label(self.frame, text=chips, borderwidth=2, relief="groove")
        self.potLabel = Label(self.frame, text=pot, borderwidth=2, relief="groove")
        self.betLabel = Label(self.frame, text=bet, borderwidth=2, relief="groove")

        self.betLabel.grid(row=5, column=2);
        self.chipsLabel.grid(row=5, column=4)
        self.potLabel.grid(row=5, column=3)

    def reset_hand(self):
        self.turn = 0

    ''' Feel like this will be pretty simple '''
    def bet(self):
        bet = bet_window()

        print(bet.get_bet_amount())
        if (int(bet.get_bet_amount()) <= Player.get_chips()):
            self.bet_amount = bet.get_bet_amount()
        self.set_labels()

    def fold(self):
        print("hello")

    def check(self):
        print("hello")

    def call(self):
        print("hello")

    def Raise(self):
        print("hello")

    def deal(self):
        Player.add_card(Table.draw_card())
        Player.add_card(Table.draw_card())

        self.player_cardone = Label(self.frame, image=ace_of_spades)
        self.player_cardtwo = Label(self.frame, image=player_CardTwo)

        self.player_cardone.grid(row=4, column=0)
        self.player_cardtwo.grid(row=4, column=1)

        print(Player.get_names())
        self.dealButton.config(state="disabled")
        Player.clear()

root = Tk()
root.title("Poker")
root.configure(background="brown")

Player = player("Kyle")
Table = table(2)

ace_of_spades = PhotoImage(file="card_pics/aceofspades.png")
two_of_spades = PhotoImage(file="card_pics/2ofspades.png")
three_of_spades = PhotoImage(file="card_pics/threeofspades.png")
four_of_spades = PhotoImage(file="card_pics/fourofspades.png")
five_of_spades = PhotoImage(file="card_pics/fiveofspades.png")

player_CardOne = PhotoImage(file="card_pics/twoofhearts.png")
player_CardTwo = PhotoImage(file="card_pics/threeofhearts.png")

root.minsize(height=417, width=467)
root.maxsize(height=417, width=467)

k = GUI(root)
root.mainloop()