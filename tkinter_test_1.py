from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry('1000x200')

def button_clicked():
    print("Hello World!")
frame_l = Frame(root, background="red")
frame_r = Frame(root, background="yellow")
frame_c = Frame(root)

button_1 = Button(frame_l, text="Hello")

button_2 = Button(frame_r, text="bye")


frame_l.pack(fill=BOTH, side=LEFT, expand=True)
frame_c.pack(fill=BOTH, side=LEFT, expand=True)
frame_r.pack(fill=BOTH, side=LEFT, expand=True)


button_1.pack(fill=BOTH, side=LEFT, expand=True)
button_2.pack(fill=BOTH, side=LEFT, expand=True)


root.mainloop()