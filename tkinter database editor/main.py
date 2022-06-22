import tkinter as tk
from tkinter import ttk

import psycopg2

data = {"user": "postgres", "password": "123", "host": "localhost", "port": "5432", "database": "postgres_db"}


def resize_window(root, wight, height):
    size = [wight, height]
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    root.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


def db_call():
    connection = psycopg2.connect(**data)
    cursor = connection.cursor()
    select_query = """SELECT * FROM mobile"""
    cursor.execute(select_query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def db_insert(record):
    connection = psycopg2.connect(**data)
    cursor = connection.cursor()
    insert_query = f""" INSERT INTO mobile (ID, MODEL, PRICE) VALUES ({record[0]}, '{record[1]}', {record[2]})"""
    cursor.execute(insert_query)
    connection.commit()
    cursor.close()
    connection.close()


def db_delete(record):
    connection = psycopg2.connect(**data)
    cursor = connection.cursor()
    delete_query = f"""Delete from mobile where id = {record[0]}"""
    cursor.execute(delete_query)
    connection.commit()
    cursor.close()
    connection.close()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        resize_window(self, 800, 350)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tree = self.create_tree_widget()
        self.tree.grid(row=0, column=0, columnspan=4, sticky="nwse")
        self.ent_id = tk.Entry(self)
        self.ent_id.grid(row=1, column=0, sticky="nwe")
        self.ent_model = tk.Entry(self)
        self.ent_model.grid(row=1, column=1, sticky="nwe")
        self.ent_price = tk.Entry(self)
        self.ent_price.grid(row=1, column=2, sticky="nwe")
        self.btn_insert = tk.Button(self, text="Добавить", command=self.add_record)
        self.btn_insert.grid(row=1, column=3, sticky="nwe")

    def create_tree_widget(self):
        columns = ('id', 'model', 'price')
        tree = ttk.Treeview(self, columns=columns, show='headings')
        tree.heading('id', text='ID')
        tree.heading('model', text='Model')
        tree.heading('price', text='Price')
        records = db_call()
        for record in records:
            tree.insert('', tk.END, values=(record[0], record[1], record[2]))
        tree.bind('<<TreeviewSelect>>', self.item_selected)
        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            db_delete(list(self.tree.item(selected_item)["values"]))
            self.tree.delete(selected_item)

    def add_record(self):
        db_insert([self.ent_id.get(), self.ent_model.get(), self.ent_price.get()])
        self.tree.insert('', 0, values=(self.ent_id.get(), self.ent_model.get(), self.ent_price.get()))
        self.ent_id.delete(0, tk.END)
        self.ent_model.delete(0, tk.END)
        self.ent_price.delete(0, tk.END)


if __name__ == '__main__':
    app = App()
    app.mainloop()
