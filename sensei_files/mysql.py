from tkinter import *
from options import *

import MySQLdb

from sensei_files.main import TabelWindow


class Base:
    def __init__(self, name_db):
        self.name_db = name_db
        self.__connection = None

    def set_status_connection(self, status):
        if status == "on":
            try:
                self.__connection = MySQLdb.connect(host="localhost",
                                                    user="root",
                                                    passwd="",
                                                    db=f"{self.name_db}")
            except MySQLdb.OperationalError:
                print("Не найдена база данных")
        elif status == "off":
            try:
                self.__connection.close()
            except AttributeError:
                print("Соединение не подключено")

    def get_connection(self):
        return self.__connection

    def get_data_query(self, tabel, atributes, sort=""):
        self.set_status_connection("on")
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(f"SELECT {','.join(atributes)} FROM {tabel} {sort}")
        data = cursor.fetchall()
        self.set_status_connection("off")
        return data

class Auth(Tk):
    def __init__(self):
        super().__init__()
        resize_window(self, 200, 150)

        self.lbl_check = None
        self.ent_login = None
        self.ent_pass = None
        self.btn_entry = None

        self.create_space()

    def create_space(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        lbl_login = Label(self, text="Login")
        lbl_login.grid(row=0, column=0)

        lbl_pass = Label(self, text="Password")
        lbl_pass.grid(row=1, column=0)

        self.lbl_check = Label(self, text="")
        self.lbl_check.grid(row=2, column=1)

        self.ent_login = Entry(self)
        self.ent_login.grid(row=0, column=1)

        self.ent_pass = Entry(self)
        self.ent_pass.grid(row=1, column=1)

        self.btn_entry = Button(self, text="Войти", command=self.editor)
        self.btn_entry.grid(row=2, column=0, )

    def editor(self):
        if self.check_data():
            self.destroy()
            tab_edit = TabelWindow()
            tab_edit.mainloop()
        else:
            self.lbl_check["text"] = "Неверный логин|пароль"

    def check_data(self):
        user = self.get_user_data()
        db = Base("library")
        data = db.get_data_query("users", ("login", "password"))
        if user in data:
            return True
        else:
            return False

    def get_user_data(self):
        user_login = self.ent_login.get()
        user_pass = self.ent_pass.get()
        return user_login, user_pass


app = Auth()
app.mainloop()
