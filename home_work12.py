from tkinter import *
from random import *
from options import *


def move(bt):
    bt.destroy()
    b = Button(root, text="go", command=lambda: move(b))
    b.place(relx=randrange(20, 80) / 100, rely=randrange(20, 80) / 100)


root = Tk()

resize_window(root, 400, 400)

btn = Button(root, text="go", command=lambda: move(btn))
btn.place(relx=0.5, rely=0.5)

root.mainloop()
