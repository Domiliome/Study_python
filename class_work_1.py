from tkinter import *
from options import *
import re


class App(Tk):
    def __init__(self):
        super().__init__()
        resize_window(self, 400, 400)
        self.create_interface()

    def create_interface(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.lbl_name = Label(self, text="ФИО")
        self.lbl_name.grid(row=0, column=0)
        self.ent_name = Entry(self)
        self.ent_name.grid(row=0, column=1)
        self.btn_name = Button(self, text="Проверить", command=self.get_fio)
        self.btn_name.grid(row=0, column=2)
        self.lbl_result = Label(self, text="", font="Tahoma 24")
        self.lbl_result.grid(row=1, column=0, columnspan=3)

    def get_fio(self):
        fio = self.check_name()
        print(f"Имя - {fio[0]}\n"
              f"Фамилия - {fio[1]}\n"
              f"Отчество - {fio[2]}")

    def check_name(self):
        name = self.ent_name.get().split()
        if len(self.ent_name.get().split(" ")) == 3:
            self.lbl_result["text"] = "Верно"
        else:
            self.lbl_result["text"] = "Неверно"
        return name[0], name[1], name[2]

def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
