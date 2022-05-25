from tkinter import *
from list_actions import ListActions

class ModelTkinter:

    def __init__(self, name, wight, height):
        self.root = Tk()
        self.root.title(name)
        self.root.resizable(False, False)
        self.root.configure(bg='#7999a4')

        # Окно по центру любого экрана #
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - (wight // 2)
        h = h - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(wight, height, w, h))

        ListActions(self.root).run()

        self.root.mainloop()

l = ModelTkinter("ListAction", 417,417)