from tkinter import *

class Table:

    def __init__(self, master):
        frame = Frame(master)

        frame.pack()

        ''' Here is where the table cards should be shown'''
        self.cardOne = Label(frame, image=CardOne)
        self.cardTwo = Label(frame, image=CardTwo)
        self.cardOne.grid(row=0)
        self.cardTwo.grid(row=0, column=1)

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

        ''' Here is where the pic of the 2 cards you have should go '''
        

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

CardOne = PhotoImage(file="card_pics/aceofspades.png")
CardTwo = PhotoImage(file="card_pics/aceofdimandos.png")
root.minsize(height=417, width=437)
root.maxsize(height=417, width=437)
k = Table(root)
root.mainloop()