from tkinter import *
from tkinter import ttk
from func import setWindow, addModal, delBook
from Books import Books


class TabelWindow(Tk):
    def __init__(self):
        super().__init__()
        books = Books()
        setWindow(self, 800, 300, 'Библиотека')
        # КОД ПРОГРАММЫ
        table = ttk.Treeview(self)
        Button(self, text="Удалить выбранную книгу", command=lambda: delBook(table, books)).pack()
        Button(self, text="Добавить книгу", command=lambda: addModal(table, self, books)).pack()
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
