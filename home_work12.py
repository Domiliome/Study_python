from tkinter import *
from random import *


def resize_window(root, wight, height):
    size = [wight, height]
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    root.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


def move(bt):
    bt.destroy()
    b = Button(root, text="go", command=lambda: move(b))
    b.place(relx=randrange(20, 80) / 100, rely=randrange(20, 80) / 100)


root = Tk()

resize_window(root, 400, 400)

btn = Button(root, text="go", command=lambda: move(btn))
btn.place(relx=0.5, rely=0.5)

root.mainloop()
