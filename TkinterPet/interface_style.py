from tkinter import Button


class MyButton(Button):
    def __init__(self, scene, color, text, command):
        super().__init__(bg=color[0],
                         fg="white",
                         command=command,
                         text=text,
                         activebackground=color[1],
                         activeforeground="white",
                         highlightbackground="white",
                         highlightcolor="white",
                         bd=0,
                         font=18)
