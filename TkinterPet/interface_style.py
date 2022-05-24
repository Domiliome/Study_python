from tkinter import Button, Label

class MyButton(Button):
    def __init__(self, scene, color, text, command):
        super().__init__(bg=color[0],
                         fg="white",
                         command=command,
                         text=text,
                         activebackground=color[1],
                         activeforeground="white",
                         bd=0,
                         font=18)

class MyLabel(Label):
    def __init__(self, scene, color, text):
        super().__init__(bg=color[0],
                         fg="white",
                         text=text,
                         activebackground=color[1],
                         activeforeground="white",
                         bd=0,
                         font=18)