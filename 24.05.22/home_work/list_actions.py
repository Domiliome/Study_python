from tkinter import *
from style1 import MyButton, MyLabel, MyText


class ListActions:
    actions = []  # Список действий
    colors = {"gray": ["df", "ds"]}

    def __init__(self, root):
        self.root = root
        self.text = None
        self.button_append = None
        self.button_print = None
        self.label_actions = None
        self.frame = None

    def run(self):
        # Область виджетов
        MyButton(self.root, text="Добавить\nдействия", command=self.add_actions)\
            .grid(column=0, row=0, sticky=N+S+W+E)
        self.text = MyText(self.root, width=20)
        self.text.grid(column=1, row=0, sticky=N+S+W+E)
        MyButton(self.root, text="Показать\nдействия", command=self.print_actions)\
            .grid(column=2, row=0, sticky=N+S+W+E)

    def add_actions(self):
        s = self.text.get(1.0, END+"-1c")
        if s != "":
            s = s.split("\n")
            self.actions.extend(s)
            self.text.delete(1.0, END)

    def print_actions(self):
        if self.label_actions is not None:
            self.label_actions.destroy()
        self.label_actions = MyLabel(self.root, text=str(self.actions))
        self.label_actions.grid(column=0, row=3, columnspan=3, rowspan=3, sticky=N + S + W + E)
