oceans = ["Pacific Ocean", "Indian Ocean"]


class Cetacean:
    i = 0
    def __init__(self, size, ocean, age):
        self.id = init_whale()
        self.__size = size
        self.__ocean = ocean
        self.__age = age


    def get_size(self):
        return self.__size

    def get_age(self):
        return self.__age

    def get_ocean(self):
        return self.__ocean
    def init_whale(self):
        i += 1
        return i
class WhiteWhale(Cetacean):
    def __init__(self, size, age):
        super().__init__(size, oceans[0], age)

    def get_name(self):
        return "Белый кит"



class Cashalot(Cetacean):
    def __init__(self, size, age):
        super().__init__(size, oceans[1], age)

    def get_name(self):
        return "Кашалот"

mobi = WhiteWhale(20, 38)
nemo = Cashalot(12, 3)

print(f"Название вида: {mobi.get_name()}\n"
      f"Возраст: {mobi.get_age()} г.\n"
      f"Вес: {mobi.get_size()} кг.)