file = open("text.txt", "w", encoding="utf8")
while True:
    data = input("Введите данные: ")
    if data == "exit":
        file.close()
        break
    file.write(data+"\n")
