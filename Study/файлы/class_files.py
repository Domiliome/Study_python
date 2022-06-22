file = open("text.txt", "w", encoding="utf8")           # открывает фаил
file.write("Hello\nHow are you?\nbye")                  # записывает в фаил
file.close()                                            # закрывает фаил

file = open("text.txt", "r", encoding="utf8")
file.seek(0)                                            # перемещает курсор
print(file.read())                                      # читает фаил
file.close()

file = open("text.txt", "a", encoding="utf8")           # a - append добавляет к существующему
file.write("\nYo\n")
file.close()
