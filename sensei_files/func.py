from tkinter import *

def setWindow(root, width, height, title):
    root.title(title)
    root.resizable(False, False)
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    x = int(ws / 2 - width / 2)
    y = int(wh / 2 - height / 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def addModal(table, root, books):
    add = Toplevel(root)
    setWindow(add, 300, 200, 'Добавление книги')
    add.transient(root)
    add.grab_set()
    Label(add, text="Название книги").pack()
    title = Entry(add)
    title.pack()
    Label(add, text="Автор книги").pack()
    author = Entry(add)
    author.pack()
    def addBook():
        books.insert(title.get(), author.get())
        last = books.getLast()
        table.insert(parent='', index='end', iid=last[0], text='', values=last)
        add.destroy()
        add.update()
    Button(add, text="Добавить", command=addBook).pack()