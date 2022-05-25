from tkinter import *
from tkinter.ttk import Style


class App(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Калькулятор на Tkinter")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        lbl_welcome = Label(self, text="Welcome to my program")
        lbl_welcome.grid(row=0, column=0, columnspan=4, sticky=S)

        txt_actions = Text(self)
        txt_actions.grid(row=1, column=0, columnspan=4, padx=5)

        btn_insert = Button(self, text="insert", width=15)
        btn_insert.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        btn_exit = Button(self, text="exit", width=15)
        btn_exit.grid(row=2, column=3, sticky=E, padx=5, pady=5)

        lbl_actions = Label(self, text="Test")
        lbl_actions.grid(row=2, column=0, columnspan=3, sticky=W, padx=5, pady=5)

        self.pack()


def main():
    root = Tk()
    App()
    root.mainloop()


if __name__ == '__main__':
    main()
