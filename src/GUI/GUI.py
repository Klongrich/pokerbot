from tkinter import *
from src.GUI.hand import current_hand
from src.GUI.table import table
from src.GUI.player import player

class GUI:

    def __init__(self, master):
        self.frame = Frame(master, background="dark green", highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
        self.frame.pack()

        ''' Here is where the table cards should be shown'''

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

        self.addButton = Button(self.frame, text="Bet", width=10, command=self.bet)
        self.addButton.grid(row=3, column=0, pady=80)

        self.addButton = Button(self.frame, text="check", width=10, command=self.check)
        self.addButton.grid(row=3, column=1)

        self.addButton = Button(self.frame, text="Fold", width=10, command=self.fold)
        self.addButton.grid(row=3, column=2)

        self.addButton = Button(self.frame, text="Call", width=10, command=self.call)
        self.addButton.grid(row=3, column=3)

        self.addButton = Button(self.frame, text="Raise", width=10, command=self.Raise)
        self.addButton.grid(row=3, column=4)

        ''' Where your cards are shown '''

        self.chipsLabel = Label(self.frame, text="Chips: 714,000")
        self.player_cardone = Label(self.frame, image=player_CardOne)
        self.player_cardtwo = Label(self.frame, image=player_CardTwo)
        self.addButton = Button(self.frame, text="Deal", width=10, command=self.deal)


        self.player_cardone.grid(row=4, column=0)
        self.player_cardtwo.grid(row=4, column=1)
        self.addButton.grid(row=4, column=4)
        self.chipsLabel.grid(row=5, column=4)

    ''' Feel like this will be pretty simple '''
    def bet(self):
        print("hello")

    def fold(self):
        print("hello")

    def check(self):
        print("hello")

    def call(self):
        print("hello")

    def Raise(self):
        print("hello")

    def deal(self):
        players_hand.add_card(Table.draw_card())
        players_hand.add_card(Table.draw_card())

        self.player_cardone = Label(self.frame, image=ace_of_spades)
        self.player_cardtwo = Label(self.frame, image=player_CardTwo)

        self.player_cardone.grid(row=4, column=0)
        self.player_cardtwo.grid(row=4, column=1)

        print(players_hand.get_names())
        players_hand.clear()

root = Tk()
root.title("Poker")
root.configure(background="brown")

human = player("Kyle")
Table = table(2)
players_hand = current_hand()

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