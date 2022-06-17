from tkinter import *
from Pet.interface_style import MyButton
from Study.HomeWork.home_work_3 import Cat


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
        self.img = None
        self.image = None

    def open_main_menu(self):
        self.play = MyButton(self.scene, self.color_play, text="ИГРАТЬ", command=self.__open_game)
        self.exit = MyButton(self.scene, self.color_exit, text="ВЫХОД", command=self.__close_game)
        self.play.pack(fill=BOTH, side=LEFT, expand=True)
        self.exit.pack(fill=BOTH, side=RIGHT, expand=True)

    def __close_game(self):
        self.scene.destroy()

    def __pause(self):
        self.canvas.destroy()
        self.button_1.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        self.button_4.destroy()
        self.button_menu.destroy()
        self.open_main_menu()

    def __open_game(self):
        self.play.destroy()
        self.exit.destroy()
        self.__begin_pet()

    def __begin_pet(self):
        cat1 = Cat("Tom")

        self.canvas = Canvas(self.scene, background=self.color_play[0], bd=0)
        self.img = PhotoImage(file="cat.png")
        self.image = self.canvas.create_image(250, 100, anchor='nw', image=self.img)
        self.button_1 = MyButton(self.scene, self.color_play, text="ПОИГРАТЬ", command=cat1.play)
        self.button_2 = MyButton(self.scene, self.color_play, text="ПОМЫТЬ", command=cat1.wash)
        self.button_3 = MyButton(self.scene, self.color_play, text="ПОСПАТЬ", command=cat1.sleep_1)
        self.button_4 = MyButton(self.scene, self.color_play, text="ПОКОРМИТЬ", command=cat1.eat)
        self.button_menu = MyButton(self.scene, self.color_exit, text="Пауза", command=self.__pause)

        self.canvas.pack(fill=BOTH, side=TOP, expand=True)
        self.button_1.pack(fill=BOTH, side=LEFT, expand=True)
        self.button_2.pack(fill=BOTH, side=LEFT, expand=True)
        self.button_3.pack(fill=BOTH, side=LEFT, expand=True)
        self.button_4.pack(fill=BOTH, side=LEFT, expand=True)
        self.button_menu.pack(fill=BOTH, side=RIGHT, expand=True)
