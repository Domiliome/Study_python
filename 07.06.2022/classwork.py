from random import *
from tkinter import *

numbers = []
rnumbers = []


def make_job():
    a = ent_numbers.get()[-6:-1] + ent_numbers.get()[-1]
    a = " ".join(a)
    a = a.split(" ")
    print(a)
    for i in range(6):
        rnumbers.append(randrange(0, 9))
    lbl_rnumbers["test"] = "".join(rnumbers)


def resize_window(window, wight, height):
    size = [wight, height]
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    window.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


root = Tk()
resize_window(root, 400, 400)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

ent_numbers = Entry(root, bg="yellow", font="Tahoma 90", justify=CENTER, width=6)
ent_numbers.grid(row=0, sticky="nswe")

lbl_rnumbers = Label(root, text="---", bg="lightblue")
lbl_rnumbers.grid(row=1, sticky="nswe")

btn_go = Button(root, text="поехали", bg="green", command=make_job)
btn_go.grid(row=2, sticky="nwse")

root.mainloop()
