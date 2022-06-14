file = open("README.md", "r")
file_text = file.read()
login = input("Введите логин")
password = input("Введите пароль")

if login and password in file_text:
    print("Вход выполнен")
else:
    print("Неверный логин или пароль")

file.close()



