import MySQLdb

class Migration:
    database = 'library'
    user = 'root'
    password = ''
    host = 'localhost'
    sql_create_books = "CREATE TABLE `library`.`books` " \
                       "(`id` INT(100) NOT NULL AUTO_INCREMENT ," \
                       " `title` VARCHAR(64) NOT NULL ," \
                       " `author` VARCHAR(64) NOT NULL ," \
                       " PRIMARY KEY (`id`)) ENGINE = InnoDB"
    sql_create_users = "CREATE TABLE `library`.`users` " \
                       "(`id` INT(50) NOT NULL AUTO_INCREMENT ," \
                       " `login` VARCHAR(20) NOT NULL ," \
                       " `password` VARCHAR(20) NOT NULL ," \
                       " PRIMARY KEY (`id`)) ENGINE = InnoDB"
    sql_insert_admin = "INSERT INTO `users` (`id`, `login`, `password`)" \
                       " VALUES (NULL, 'admin', 'admin')"
    def copy(self):
        try:
            connection = MySQLdb.connect(
                self.host,
                self.user,
                self.password,
                self.database
            )
            cursor = connection.cursor()
            cursor.execute(self.sql_create_books)
            cursor.execute(self.sql_create_users)
            cursor.execute(self.sql_insert_admin)
            connection.commit()
            connection.close()
        except MySQLdb.OperationalError:
            print("Миграция уже произошла")