import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="localhost",
                                  port="5432",
                                  database="postgres_db")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    select_query = """SELECT * FROM mobile"""
    cursor.execute(select_query)

    rows = cursor.fetchall()

    for row in rows:
        print("Id - ", row[0])
        print("Model - ", row[1])
        print("Price - ", row[2], "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")