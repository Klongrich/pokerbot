from tkinter import *

class bet_window:

    bet = 0

    def __init__(self):
        self.master = Tk()
        self.master.title("Bet")
        Label(self.master, text="Enter Amount").grid(row=0)
        Button(self.master, text="Enter", command=self.set_bet_amount).grid(row=1, column=0)
        Button(self.master, text="Cancle", command=quit).grid(row=1, column=1)
        self.e1 = Entry(self.master)
        self.e1.grid(row=0, column=1)
        mainloop()

    def set_bet_amount(self):
        self.bet = self.e1.get()
        self.master.quit()


    def get_bet_amount(self):
        return self.bet

    def printstuff(self):
        print("he")

