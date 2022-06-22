import sqlite3 as sql


print("1 - добавление\n2 - получение")
choice = int(input("> "))

con = sql.connect("test.bd")

with con:

    if choice == 1:
        name = input("Name\n> ")
        surname = input("Surname\n> ")

    elif choice == 2:

        for row in rows:
            print(row[0], row[1])
    else:
        print("Вы ошиблись")
