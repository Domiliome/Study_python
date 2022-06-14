Я хочу чтобы польз вводил логин и пароль и эти данные записывались в фаил

file = open("README.md", "a")
login = input("Введите логин")
password = input("Введите пароль")

file.write(f"{login} {password}")

file.close()
