from tkinter import *

from style import MyButton, MyLabel, MySubButton, ActionButton


def resize_window(window, wight, height):
    size = [wight, height]
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    window.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


def del_action(action, window):
    complete_actions.append(action)
    actions.remove(action)
    action.destroy()
    window.destroy()
    canvas.configure(scrollregion=canvas.bbox("all"))


def add_action(name, description, window):
    actions.append(Action(actions_frame, name, description))
    window.destroy()
    print(actions[0].description)
    canvas.configure(scrollregion=canvas.bbox("all"))


def action_menu(action):
    action_window = Toplevel()
    resize_window(action_window, 400, 200)
    action_window.grab_set()
    action_window["bg"] = "#ccc1c1"

    action_window.grid_columnconfigure(0, weight=1)
    action_window.grid_columnconfigure(1, weight=1)
    action_window.grid_columnconfigure(2, weight=1)
    action_window.grid_columnconfigure(3, weight=1)
    action_window.grid_rowconfigure(0, weight=1)
    action_window.grid_rowconfigure(1, weight=2)
    action_window.grid_rowconfigure(2, weight=2)

    lbl_name = MyLabel(action_window, text="название:")
    lbl_name.grid(row=0, column=0, sticky="e")

    ent_name_action = Entry(action_window, width=1)
    ent_name_action.grid(row=0, column=1, columnspan=3, sticky="we")

    txt_description = Text(action_window, width=1, height=1)
    txt_description.grid(row=1, column=0, columnspan=4, sticky="nswe")

    btn_close = MySubButton(action_window, text="закрыть", command=action_window.destroy)
    btn_close.grid(row=2, column=2, columnspan=2, sticky="nswe")
    if action == btn_add_action:
        btn_add = MySubButton(action_window, text="добавить",
                              command=lambda: add_action(ent_name_action.get(), txt_description.get(1.0, END),
                                                         action_window))
        btn_add.grid(row=2, column=0, columnspan=2, sticky="nswe")
    else:
        btn_delete = MySubButton(action_window, text="выполнено", command=lambda: del_action(action, action_window))
        btn_delete.grid(row=2, column=0, columnspan=2, sticky="nswe")
        ent_name_action.insert(0, action.name)
        ent_name_action["state"] = DISABLED
        txt_description.insert(1.0, action.description)
        txt_description["state"] = DISABLED


def history_menu():
    history_window = Toplevel()
    resize_window(history_window, 600, 400)
    history_window.grab_set()

    for thing in range(len(complete_actions)):
        MyLabel(history_window, text=complete_actions[thing].name).grid(row=thing, column=0)
        MyLabel(history_window, text="20.12.2020").grid(row=thing, column=1)


def on_mousewheel(event):
    if len(actions) > 3:
        canvas.yview_scroll(-1 * (event.delta // 120), "units")
    canvas.configure(scrollregion=canvas.bbox("all"))


class Action(ActionButton):
    def __init__(self, master, name, description):
        super().__init__(master=master, text=name, command=lambda: action_menu(self))
        self.name = name
        self.description = description
        self.grid(sticky="we")


actions = []
complete_actions = []

root = Tk()
resize_window(root, 600, 400)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

main_frame = Frame(root)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=5)

sub_frame = Frame(root)
sub_frame.grid_columnconfigure(0, weight=1)
sub_frame.grid_rowconfigure(0, weight=1)
sub_frame.grid_rowconfigure(1, weight=1)
sub_frame.grid_rowconfigure(2, weight=1)
sub_frame.grid_rowconfigure(3, weight=1)
sub_frame.grid_rowconfigure(4, weight=1)

btn_history = MySubButton(master=sub_frame, text="История", command=lambda: history_menu())
btn_history.grid(row=0, column=0, sticky="NSWE")

btn_unk1 = MySubButton(master=sub_frame, text="...")
btn_unk1.grid(row=1, column=0, sticky="NSWE")
btn_unk2 = MySubButton(master=sub_frame, text="...")
btn_unk2.grid(row=2, column=0, sticky="NSWE")
btn_unk3 = MySubButton(master=sub_frame, text="...")
btn_unk3.grid(row=3, column=0, sticky="NSWE")

btn_quit = MySubButton(master=sub_frame, text="Выход", command=lambda: root.destroy())
btn_quit.grid(row=4, column=0, sticky="NSWE")

lbl_my_actions = MyLabel(master=main_frame, text="Мои задачи")
lbl_my_actions.grid(row=0, column=0, sticky="NSWE")

canvas = Canvas(main_frame, highlightthickness=0)
canvas["bg"] = "#ccc1c1"
canvas.grid(row=1, column=0, sticky="NSWE")

main_frame.grid(row=0, column=0, sticky="NSWE")
sub_frame.grid(row=0, column=1, sticky="NSWE")

canvas.grid_columnconfigure(0, weight=1)
canvas.grid_rowconfigure(0, weight=1)

scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

actions_frame = Frame(canvas, bg="black")

canvas.create_window((0, 0), window=actions_frame, anchor="nw")
canvas.bind_all("<MouseWheel>", on_mousewheel)

btn_add_action = ActionButton(actions_frame, text="+", command=lambda: action_menu(btn_add_action))
btn_add_action.grid(row=0, column=0, sticky="swen")

root.mainloop()
