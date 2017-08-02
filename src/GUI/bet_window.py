from tkinter import *

def get_bet_amount():
    print(e1.get())

master = Tk()
Label(master, text="Enter Amount").grid(row=0)
Button(master, text="Enter", command=get_bet_amount).grid(row=1, column=0)
Button(master, text="Cancle", command=quit).grid(row=1, column=1)
e1 = Entry(master)
e1.grid(row=0, column=1)

mainloop()