from tkinter import *
from options import *
from random import *


class App(Tk):
    def __init__(self):
        self.result_arr = []
        super().__init__()
        resize_window(self, 200, 200)
        self.btn = Button(self, text="Get", command=self.get_number)
        self.btn.pack(expand=1)
        self.lbl = Label(self, text="", font="Tahoma 24")
        self.lbl.pack(expand=1)

    def get_number(self):
        n = randrange(1, 100)
        self.lbl["text"] = n
        if n % 2 == 0:
            self.result_arr.append(n)
        print(self.result_arr)


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
