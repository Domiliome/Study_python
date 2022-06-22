# Выполнение SQL-запроса для вставки данных в таблицу
    insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (2, 'Iphone 10',40000)"""
    cursor.execute(insert_query)
    connection.commit()
    print("Первая запись успешно создана")
    cursor.execute("SELECT * from mobile")
    record = cursor.fetchall()
    print("Результат", record)

# Выполняем SQL-запрос для обновления таблицы
    update_query = """Update mobile set price = 9000 where id = 1"""
    cursor.execute(update_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Запись успешно изменена")

# Выполняем запрос на удаление записи с таблицы
    delete_query = """Delete from mobile where id = 1"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Запись успешно удалена")