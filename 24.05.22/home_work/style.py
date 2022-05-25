# Классы стилизованных виджетов
from tkinter import Button, Label, Frame, Text


class MyButton(Button):
    def __init__(self, scene, color="#7999a4", text="", command=""):
        super().__init__(bg=color,
                         fg="BLACK",
                         width=10,
                         command=command,
                         text=text,
                         bd=0,
                         font=18)


class MyLabel(Label):
    def __init__(self, scene, color="#7999a4", text=""):
        super().__init__(bg=color,
                         fg="BLACK",
                         text=text,
                         font=0)


class MyFrame(Frame):
    def __init__(self, scene, color="WHITE"):
        super().__init__(bg=color,
                         bd=0, )


class MyText(Text):
    def __init__(self, scene, width, color="#e6ecee"):
        super().__init__(bg=color,
                         bd=2,
                         width=width)
