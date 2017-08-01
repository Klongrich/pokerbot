from tkinter import *

class Table:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        ''' Here is where the table cards should be shown'''
        self.cardOne = Label(frame, image=CardOne)
        self.cardTwo = Label(frame, image=CardTwo)
        self.cardThree = Label(frame, image=CardThree)
        self.cardFour = Label(frame, image=CardFour)
        self.cardFive = Label(frame, image=CardFive)

        self.cardOne.grid(row=0)
        self.cardTwo.grid(row=0, column=1)
        self.cardThree.grid(row=0, column=2)
        self.cardFour.grid(row=0, column=3)
        self.cardFive.grid(row=0, column=4)


        ''' All the buttons for doing stuff'''
        self.chipsLabel = Label(frame, text="Amount Of Chips: 714,000")
        self.chipsLabel.grid(row=1, column=1)

        self.addButton = Button(frame, text="Bet", width=14, command=self.bet)
        self.addButton.grid(row=2, column=0)

        self.addButton = Button(frame, text="check", command=self.check)
        self.addButton.grid(row=2, column=1)

        self.addButton = Button(frame, text="Fold", command=self.fold)
        self.addButton.grid(row=2, column=2)

        self.addButton = Button(frame, text="Call", command=self.call)
        self.addButton.grid(row=2, column=3)

        self.addButton = Button(frame, text="Raise", command=self.Raise)
        self.addButton.grid(row=2, column=4)

        ''' Where your cards are shown '''

        self.player_cardone = Label(frame, image=player_CardOne)
        self.player_cardtwo = Label(frame, image=player_CardTwo)

        self.player_cardone.grid(row=3, column=0)
        self.player_cardtwo.grid(row=3, column=1)



    ''' Feel like this will be pretty simple '''
    def bet(self):
        print("hello");

    def fold(self):
        print("hello");

    def check(self):
        print("hello");

    def call(self):
        print("hello");

    def Raise(self):
        print("hello");

root = Tk()
root.title("Poker")

CardOne = PhotoImage(file="card_pics/aceofspades.png")
CardTwo = PhotoImage(file="card_pics/2ofspades.png")
CardThree = PhotoImage(file="card_pics/threeofspades.png")
CardFour = PhotoImage(file="card_pics/fourofspades.png")
CardFive = PhotoImage(file="card_pics/aceofspades.png")

player_CardOne = PhotoImage(file="card_pics/twoofhearts.png")
player_CardTwo = PhotoImage(file="card_pics/threeofhearts.png")
root.minsize(height=417, width=467)
root.maxsize(height=417, width=467)
k = Table(root)
root.mainloop()