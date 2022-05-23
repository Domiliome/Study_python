class Pet:
    move = ""
    mood = 0
    feel = 0
    fresh = 0
    sleep = 0

    def __init__(self, name):
        self.__name = name

    def eat(self):
        self.feel += 5
        self.sleep += 1
        self.fresh -= 2

    def wash(self):
        self.fresh += 5
        self.sleep += 1

    def sleep_1(self):
        self.sleep -= 5
        self.feel -= 1

    def play(self):
        self.fresh -= 5
        self.sleep += 5
        self.mood += 2

    def change_move(self):
        if self.move == "покормить":
            self.eat()
        elif self.move == "помыть":
            self.wash()
        elif self.move == "поспать":
            self.sleep_1()
        elif self.move == "поиграть":
            self.play()

    def status(self):
        self.non_neg_status()
        if self.sleep > 7:
            return "Питомец хочет спать"
        elif self.fresh < 2:
            return "Питомец грязный
        elif self.feel < 3:
            return "Питомец голоден
        elif self.mood < 2:
            return "Питомец скучает"
        else:
            "Питомец доволен"
        print("Настроение ", self.mood,
              "\nСамочувствие ", self.feel,
              "\nСвежесть ", self.fresh,
              "\nСонливость ", self.sleep)

    def non_neg_status(self):
        if self.mood < 0: self.mood = 0
        if self.feel < 0: self.feel = 0
        if self.fresh < 0: self.fresh = 0
        if self.sleep < 0: self.sleep = 0


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def sleep_1(self):
        self.sleep -= 7
        self.feel -= 2

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        self.fresh -= 5
        self.sleep += 5
        self.mood += 7


pet1 = Dog("Sam")
while True:
    pet1.move = input("Введите действие ")
    pet1.change_move()
    pet1.status()
