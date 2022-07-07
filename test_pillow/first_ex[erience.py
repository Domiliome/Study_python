from tkinter import *
from PIL import Image, ImageFilter, ImageTk

root = Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
my_image = Image.open("copy.png")
tk_image_1 = ImageTk.PhotoImage(my_image)

pic = Label(root, image=tk_image_1, bg='#000', anchor="center")
pic.grid(row=0, column=0, sticky="nwse")

root.mainloop()
