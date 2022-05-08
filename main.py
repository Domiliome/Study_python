def main():
    list = []
    a = input("Первая строка: ").lower()
    b = input("Вторая строка: ").lower()
    c = whoLonger(a, b)
    c = c[0:20]                             # Срез лишней части
    print("Выбранная строка: ", c)
    print("Число символов: ", len(c))
    a = input("Искомый символ: ")

    for i in range(len(c)):                 #
        if c[i] == a:                       # Цикл поиска символа в строке
            list.append(i)                  #

    print("Повторения: ", list)             # Вывод результата


def whoLonger(a, b):                        #
    if len(a) > len(b):                     #
        return a                            # Функция выбора большей строки
    else:                                   #
        return b                            #


if __name__ == '__main__':
    main()
