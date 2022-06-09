from tkinter import *


def print_hello(event):
    button["bg"] = "#4e748e"


def print_bye(event):
    button["bg"] = "#1c2732"


def resize_window(root, wight, height):
    size = [wight, height]
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    root.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


root = Tk()
resize_window(root, 300, 300)

button = Button(root, text="CLICK", width=10, height=1, bd=0, bg="#1c2732", fg="#fff", font=12,activebackground="#7aa5bc")
button.pack(expand=True, fill=X)
button.bind('<Enter>', print_hello)
button.bind('<Leave>', print_bye)

root.mainloop()
