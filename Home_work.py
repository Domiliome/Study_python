from tkinter import *
from options import *


class App(Tk):
    def __init__(self):
        super().__init__()

        self.exp = [""]
        operations = ["%", "c", "<", "d", "k", "q", "/", "7",
                      "8", "9", "*", "4", "5", "6", "-", "1",
                      "2", "3", "+", "z", "0", ",", "="]
        btns = []

        resize_window(self, 320, 430)
        self.overrideredirect(True)
        self.config(bg="#1F1F1F")
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=4)
        self.grid_rowconfigure(3, weight=4)
        self.grid_rowconfigure(4, weight=4)
        self.grid_rowconfigure(5, weight=4)
        self.grid_rowconfigure(6, weight=4)
        self.grid_rowconfigure(7, weight=4)

        self.panel()

        self.lbl_result = Label(self, text="", font="Tahoma 25 ", anchor="e", bd=0, bg="#1F1F1F", fg="#FFF")
        self.lbl_result.grid(row=1, column=0, columnspan=4, sticky="nwse", pady=1, padx=1)
        # Создание кнопок калькулятора
        for i in range(2, 8):
            for j in range(4):
                if i == 2 and j == 2:
                    continue
                btn = Button(self, text=f"{i} - {j}", bd=0, bg="#131313", fg="#FFF", font="Tahoma 10",
                             activebackground="#494949", activeforeground="#FFF")
                if (4 <= i <= 7) and (j < 3):
                    btn["bg"] = "#060606"
                if i == 2 and j == 1:
                    btn.grid(row=i, column=j, columnspan=2, sticky="nwse", pady=1, padx=1)
                else:
                    btn.grid(row=i, column=j, sticky="nwse", pady=1, padx=1)
                btns.append(btn)
        # Придаём кнопкам анимацию, название и команды
        for i in range(len(btns)):
            match btns[i]["bg"]:
                case "#131313":
                    btns[i].bind('<Enter>', lambda event, b=btns[i]: b.config(bg="#343434"))
                    btns[i].bind('<Leave>', lambda event, b=btns[i]: b.config(bg="#131313"))
                case "#060606":
                    btns[i].bind('<Enter>', lambda event, b=btns[i]: b.config(bg="#343434"))
                    btns[i].bind('<Leave>', lambda event, b=btns[i]: b.config(bg="#060606"))
            btns[i].config(text=operations[i], command=lambda b=btns[i]: self.calculate(b["text"]))
            print(btns[i]["text"], " - ", btns.index(btns[i]))
        # Меняем команды "особых" кнопок
        btns[1]["command"] = lambda b=btns[1]: self.exp.clear()
        btns[2]["command"] = self.back

    # создаём рамку покруче чем у tkinter
    def panel(self):
        frm_menu = Frame(self, bg="#1F1F1F")
        frm_menu.grid(row=0, column=0, columnspan=4, sticky="nwse")
        frm_menu.grid_columnconfigure(0, weight=10)
        frm_menu.grid_columnconfigure(1, weight=1)
        frm_menu.grid_rowconfigure(0, weight=1)

        def on_mouse_down(event):
            global dif_x, dif_y
            win_position = [int(coord) for coord in self.wm_geometry().split('+')[1:]]
            dif_x, dif_y = win_position[0] - event.x_root, win_position[1] - event.y_root

        def update_position(event):
            self.wm_geometry("+%d+%d" % (event.x_root + dif_x, event.y_root + dif_y))

        frm_menu.bind('<ButtonPress-1>', on_mouse_down)
        frm_menu.bind('<B1-Motion>', update_position)
        btn_exit = Button(frm_menu, bd=0, text="×", bg="#1F1F1F",
                          fg="#FFF", font="Tahoma 10 bold",
                          activebackground="#F1707A",
                          activeforeground="#FFF",
                          command=self.destroy)
        btn_exit.grid(row=0, column=1, sticky="nwse")
        btn_exit.bind('<Enter>', lambda event: btn_exit.config(bg="#E81123"))
        btn_exit.bind('<Leave>', lambda event: btn_exit.config(bg="#1F1F1F"))

    def calculate(self, symbol):
        try:
            str1 = "".join(self.exp[1:])
            match symbol:

                case "=":
                    self.lbl_result["text"] = str(eval(str1))
                    self.exp = ['']
                case _:
                    if self.exp == ['']:
                        self.lbl_result["text"] = ""
                    self.lbl_result["text"] += symbol
                    self.exp.append(symbol)
        except ZeroDivisionError:
            self.lbl_result["text"] = "Деление на 0"
            self.exp = ['']

    def back(self):
        self.exp.pop(-1) if len(self.exp) != 1 else False
        self.lbl_result["text"] = self.lbl_result["text"][:-1]


if __name__ == '__main__':
    app = App()
    app.mainloop()
