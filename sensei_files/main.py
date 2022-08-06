from tkinter import *
from tkinter import ttk
from func import setWindow, addModal
from Books import Books

mainWindow = Tk()
books = Books()
setWindow(mainWindow, 800, 300, 'Библиотека')
#КОД ПРОГРАММЫ
table = ttk.Treeview(mainWindow)
Button(mainWindow, text="Добавить книгу", command=lambda: addModal(table, mainWindow, books)).pack()
columns = []
for column in books.labels.keys():
    columns.append(column)
table['columns'] = columns
table.column('#0', width=0, stretch=NO)
table.heading('#0', text='')
for column in columns:
    table.column(column, anchor=CENTER, width=150)
    table.heading(column, text=books.labels[column], anchor=CENTER)
for row in books.getAllBooks():
    table.insert(parent='', index='end', iid=row[0], text='', values=row)
table.pack()
#КОНЕЦ ПРОГРАММЫ
mainWindow.mainloop()