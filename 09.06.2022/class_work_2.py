from tkinter import *
from datetime import *


def resize_window(window, wight, height):
    size = [wight, height]
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    window.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


def birthday(date_birthday):
    try:
        date_list = date_birthday.split(" ")
        date1 = datetime(2022, int(date_list[1]), int(date_list[0]))
        date2 = datetime.today()
        date3 = datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]))
        result = int(date1.timestamp() - date2.timestamp()) // 3600
        if result > 0:
            lbl_result["text"] = int(date1.timestamp() - date2.timestamp()) // 3600
        else:
            lbl_result["text"] = 8760 - (-1 * (int(date1.timestamp() - date2.timestamp()) // 3600))

        lbl_result1["text"] = int(date2.timestamp() - date3.timestamp()) // 3600 // 24 // 365
    except:
        lbl_result["text"] = "None"
        lbl_result1["text"] = "None"


root = Tk()
resize_window(root, 400, 200)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

lbl_birthday = Label(root, text="Введите дату рождения")
lbl_birthday.grid(row=0, column=0)

ent_birthday = Entry(root)
ent_birthday.grid(row=0, column=1, sticky="nswe")

btn_birthday = Button(root, text="посчитать", command=lambda: birthday(ent_birthday.get()))
btn_birthday.grid(row=1, column=0, sticky="nswe")

lbl_desc = Label(root, text="Количество часов до дня рождения")
lbl_desc.grid(row=3, column=0)

lbl_result = Label(root)
lbl_result.grid(row=3, column=1)

lbl_desc1 = Label(root, text="Количество лет")
lbl_desc1.grid(row=2, column=0)

lbl_result1 = Label(root)
lbl_result1.grid(row=2, column=1)

root.mainloop()
