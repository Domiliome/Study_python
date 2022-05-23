from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry('300x40')

def button_clicked():
    print("Hello World!")

button1 = Button(root, text="Press Me", command=button_clicked)
button2 = Button(root, text="Press Me", command=button_clicked)
button3 = Button(root, text="Press Me", command=button_clicked)
button4 = Button(root, text="Press Me", command=button_clicked)
lbl = Label(root, text="Привет")
button.pack(fill=BOTH)
lbl.pack()

root.mainloop()