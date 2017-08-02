from tkinter import *

class bet_window:

    bet = 0

    def __init__(self):
        master = Tk()
        master.title("Bet")
        Label(master, text="Enter Amount").grid(row=0)
        Button(master, text="Enter", command=self.set_bet_amount).grid(row=1, column=0)
        Button(master, text="Cancle", command=quit).grid(row=1, column=1)
        self.e1 = Entry(master)
        self.e1.grid(row=0, column=1)
        mainloop()

    def set_bet_amount(self):
        self.bet = self.e1.get()

    def get_bet_amount(self):
        return self.bet

    def printstuff(self):
        print("he")

