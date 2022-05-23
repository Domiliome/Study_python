from tkinter import *
from TkinterPet.game_scene import Game


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tkinter Pat")
        self.root.resizable()

        # Окно по центру любого экрана #
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 300
        h = h - 200
        self.root.geometry('600x400+{}+{}'.format(w, h))

        game_space = Game(self.root)
        game_space.open_main_menu()

        self.root.mainloop()

test = MainWindow()