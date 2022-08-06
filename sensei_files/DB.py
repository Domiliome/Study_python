import MySQLdb
class DB:
    database = 'library'
    user = 'root'
    password = ''
    host = 'localhost'
    def __getConntection(self):
        return MySQLdb.connect(
            self.host,
            self.user,
            self.password,
            self.database
        )

    def execute(self, sql):
        self.connection = self.__getConntection()
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        self.connection.close()
        return cursor

    def fetchAll(self, sql):
        cursor = self.execute(sql)
        return cursor.fetchall()

    def fetchOne(self, sql):
        cursor = self.execute(sql)
        return cursor.fetchone()