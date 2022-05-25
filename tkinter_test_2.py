from tkinter import *
from tkinter.ttk import Style


class App(Frame):
    actions = []

    def __init__(self):
        super().__init__()
        self.lbl_actions = None
        self.txt_actions = None
        self.initUI()

    def initUI(self):

        self.master.title("Action List")
        self.style_sub(self)
        self.style_sub(self.master)

        Style().configure("TButton", padding=(0, 5, 0, 5))

        lbl_welcome = Label(self, text="WELCOME")
        lbl_welcome.grid(row=0, column=0, columnspan=4, sticky=S, pady=5)
        self.style_sub(lbl_welcome)

        self.txt_actions = Text(self, width=70, height=25)
        self.txt_actions.grid(row=1, column=0, columnspan=4, padx=5)
        self.style_main(self.txt_actions)

        btn_insert = Button(self, text="INSERT", width=10, command=self.insert_actions)
        btn_insert.grid(row=2, column=2, sticky="W", padx=5, pady=20)
        self.style_main(btn_insert)

        btn_show = Button(self, text="SHOW", width=10, command=self.show_actions)
        btn_show.grid(row=2, column=2, sticky="E", padx=5, pady=20)
        self.style_main(btn_show)

        btn_exit = Button(self, text="EXIT", width=10, command=self.master.quit)
        btn_exit.grid(row=2, column=3, sticky=E, padx=5, pady=20)
        self.style_main(btn_exit)

        self.lbl_actions = Label(self, text="")
        self.lbl_actions.grid(row=2, column=0, columnspan=3, sticky=W, padx=5, pady=5)
        self.style_sub(self.lbl_actions)

        self.pack()

    def insert_actions(self):
        s = self.txt_actions.get(1.0, END + "-1c")
        if s != "":
            s = s.split("\n")
            for i in range(len(s)):
                s[i] = s[i].strip()
            s = list(filter(None, s))

            self.actions.extend(s)
            self.txt_actions.delete(1.0, END)
        self.lbl_actions["text"] = f"Count actions: {len(self.actions)}"

    def show_actions(self):
        actions_view = Toplevel(self.master)
        self.style_sub(actions_view)

        resize_window(actions_view, 150, 250)

        actions_view.focus_set()
        actions_view.grab_set()

        lbl_act = Label(master=actions_view, text="ACTIONS")
        lbl_act.pack(side=TOP, padx=5, pady=5)
        self.style_sub(lbl_act)

        listbox = Listbox(actions_view)
        for i in range(len(self.actions)):
            listbox.insert(i, self.actions[i])
        listbox.pack(side=TOP)
        self.style_main(listbox)

        btn_exit = Button(master=actions_view, text="QUIT", command=actions_view.destroy)
        btn_exit.pack(side=TOP, padx=5, pady=5)
        self.style_main(btn_exit)

    def style_main(self, widget):
        widget["background"] = "#ef9740"
        if widget.widgetName == "button":
            widget["activebackground"] = "#f3b271"
            widget["bd"] = 0

    def style_sub(self, widget):
        widget["background"] = "#f5c492"


def resize_window(root, wight, heigth):
    size = [wight, heigth]
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    root.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


def main():
    root = Tk()
    resize_window(root, 600, 500)
    App()
    root.mainloop()


if __name__ == '__main__':
    main()
