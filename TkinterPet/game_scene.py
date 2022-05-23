from tkinter import *
from TkinterPet.interface_style import MyButton
from home_work_3 import Cat


class Game():
    def __init__(self, scene):
        self.scene = scene
        self.color_play = ["#5e9a86", "#b6d2c9"]
        self.color_exit = ["#ca3b2f", "#e8a5a0"]

        self.play = None
        self.exit = None

        self.canvas = None

        self.label_mood = None
        self.label_feel = None
        self.label_fresh = None
        self.label_sleep = None

    def open_main_menu(self):
        self.play = MyButton(self.scene, self.color_play, text="ИГРАТЬ", command=self.__open_game)
        self.exit = MyButton(self.scene, self.color_exit, text="ВЫХОД", command=self.__close_game)
        self.play.pack(fill=BOTH, side=LEFT, expand=True)
        self.exit.pack(fill=BOTH, side=RIGHT, expand=True)

    def __close_game(self):
        self.scene.destroy()

    def __open_game(self):
        self.play.destroy()
        self.exit.destroy()
        self.begin_pet()

    def __begin_pet(self):
        cat1 = Cat("Tom")



