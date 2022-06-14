from tkinter import *
import time


def resize_window(window, wight, height):
    size = [wight, height]
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    window.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))

def ticktock():
    lbl_clock["text"] = time.strftime("%H : %M : %S")
    lbl_clock.after(200, ticktock)

root=Tk()
resize_window(root, 400, 300)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

lbl_clock = Label(root, font=("Arial", 50))
lbl_clock.grid(row=0, column=0, sticky="nswe")

ticktock()

root.mainloop()
