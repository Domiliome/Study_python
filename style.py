import random
from tkinter import Button, Label

FONT = ("Comfortaa")
CLR = ["#ccc1c1", "#eae5e5", "#93ce4f", "#b5dd87"]
RC = [["#FFA24C", "#ffc289"], ["#28C0CB", "#9de6eb"], ["#a05fe8", "#c298f0"]]


class MyButton(Button):
    def __init__(self, master, text, command="", anchor="center", width=0, height=0):
        super().__init__(master=master, text=text, command=command,
                         anchor=anchor, width=width, height=height)
        self["font"] = FONT
        self["bg"] = CLR[0]
        self["bd"] = 0
        self.bind("<Enter>", lambda e: self.configure(bg=CLR[1]))
        self.bind("<Leave>", lambda e: self.configure(bg=CLR[0]))


class MySubButton(Button):
    def __init__(self, master, text, command="", anchor="center", width=0, height=0):
        super().__init__(master=master, text=text, command=command,
                         anchor=anchor, width=width, height=height)

        self["font"] = FONT
        self["bg"] = CLR[2]
        self["activebackground"] = CLR[3]
        self["bd"] = 0
        self.bind("<Enter>", lambda e: self.configure(bg=CLR[3]))
        self.bind("<Leave>", lambda e: self.configure(bg=CLR[2]))


class ActionButton(Button):
    def __init__(self, master, text, command):
        super().__init__(master=master, text=text, command=command,
                         width=200,
                         height=2,
                         anchor="w",
                         padx= 20)
        self["bd"] = 0
        self["font"] = ("Comfortaa", 16)
        random_color = random.choice(RC)
        self.configure(bg=random_color[0], activebackground=random_color[1])


class MyLabel(Label):
    def __init__(self, master, text):
        super().__init__(master=master, text=text)
        self["font"] = FONT
        self["bg"] = CLR[2]
