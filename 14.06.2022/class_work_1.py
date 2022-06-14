from datetime import datetime
from tkinter import *

# {"name": "user", "message": "Hello", "datetime": "841241242"}
user = []


def resize_window(window, wight, height):
    size = [wight, height]
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    window.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


def welcome():
    if btn_login["text"] == "Войти":
        ent_login.configure(state=DISABLED)
        btn_login["text"] = "Выйти"
    else:
        ent_login.configure(state=NORMAL)
        ent_login.delete(0, END)
        btn_login["text"] = "Войти"


def send():
    user.append(dict({"name": ent_login.get(),
                      "message": ent_send.get(),
                      "datetime": datetime.now()}))
    txt_chat.delete(1.0, END)
    for thing in user:
        txt_chat.insert(1.0, thing.get("datetime").strftime("%H:%M:%S") + " - "
                        + thing.get("name") + ": "
                        + thing.get("message") + "\n")


root = Tk()
resize_window(root, 600, 600)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=2)
root.grid_rowconfigure(2, weight=3)

lbl_send = Label(root, text="Сообщение: ")
lbl_send.grid(row=0, column=0)
ent_send = Entry(root)
ent_send.grid(row=0, column=1)

btn_send = Button(root, text="Отправить", width=20, height=5, command=send)
btn_send.grid(row=1, column=0, columnspan=2)

lbl_login = Label(root, text="Имя: ")
lbl_login.grid(row=0, column=2)

ent_login = Entry(root)
ent_login.grid(row=0, column=3)

btn_login = Button(root, text="Войти", width=20, height=5, command=welcome)
btn_login.grid(row=1, column=2, columnspan=2)

txt_chat = Text(root)
txt_chat.grid(row=2, column=0, columnspan=4)

root.mainloop()
