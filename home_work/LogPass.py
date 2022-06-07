from tkinter import *


def reg_data(sub, name, log, password):
    file = open("data.txt", "a")
    file.write(f"{name}, {log}, {password}\n")
    file.close()
    sub.destroy()


def reg_window():
    sub = Toplevel(root)
    resize_window(sub, 200, 100)

    lbl_name = Label(sub, text="ФИО")
    lbl_name.grid(row=0, column=0)
    ent_name = Entry(sub)
    ent_name.grid(row=0, column=1)

    lbl_log = Label(sub, text="Логин")
    lbl_log.grid(row=1, column=0)
    ent_log = Entry(sub)
    ent_log.grid(row=1, column=1)

    lbl_pass = Label(sub, text="Пароль")
    lbl_pass.grid(row=2, column=0)
    ent_pass = Entry(sub)
    ent_pass.grid(row=2, column=1)

    btn_add = Button(sub, text="Добавить", command=lambda: reg_data(sub,
                                                                    ent_name.get(),
                                                                    ent_log.get(),
                                                                    ent_pass.get()))
    btn_add.grid(row=3, column=0, columnspan=2)


def log_data(log, password):
    file = open("data.txt", "r")

    data = file.read()
    data = data.split("\n")
    file.close()
    data.pop(-1)
    for thing in data:
        thing.split(",")

    for i in range(len(data)):
        if log in data[i] and password in data[i] and log != "" and password != "":
            lbl_status["text"] = "Успешно"
            break
        else:
            lbl_status["text"] = "Неверно"


def resize_window(window, wight, height):
    size = [wight, height]
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    window.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


root = Tk()
resize_window(root, 500, 200)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

lbl_status = Label(root)
lbl_status.grid(row=2, column=1)
lbl_log = Label(root, text="логин")
lbl_log.grid(row=0, column=0)

lbl_reg = Label(root, text="пароль")
lbl_reg.grid(row=1, column=0)

ent_log = Entry(root)
ent_log.grid(row=0, column=1, columnspan=2, sticky="we")

ent_pass = Entry(root)
ent_pass.grid(row=1, column=1, columnspan=2, sticky="we")

btn_log = Button(master=root, text="войти", command=lambda: log_data(ent_log.get(),
                                                                     ent_pass.get()))
btn_log.grid(row=2, column=0, sticky="WE")

btn_reg = Button(master=root, text="регистрация", command=lambda: reg_window())
btn_reg.grid(row=2, column=2, sticky="WE")

root.mainloop()
