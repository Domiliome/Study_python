from DB import DB
from migration import *


class Books(DB):
    data = Migration()
    data.copy()
    table = 'books'
    labels = dict(
        {
            'id': 'ID',
            'title': 'Название книги',
            'author': 'Автор книги'
        }
    )

    def getLast(self):
        return self.fetchOne('SELECT * FROM ' + self.table + ' ORDER BY id DESC')

    def getAllBooks(self):
        return self.fetchAll('SELECT * FROM ' + self.table)

    def insert(self, title, author):
        sql = f"INSERT INTO {self.table} (id, title, author) VALUES (NULL, '{title}', '{author}')"
        return self.execute(sql)

    def delete(self, id):
        sql = f"DELETE FROM {self.table} WHERE id = {id}"
        return self.execute(sql)
