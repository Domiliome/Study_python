class Pet:
    move = ""

    mood = 3
    feel = 2
    fresh = 0
    sleep = 10

    def __init__(self, name):
        self.name = name

    def eat(self):
        self.feel += 5
        self.sleep += 1
        self.fresh -= 2

    def wash(self):
        self.fresh += 5
        self.sleep += 1

    def sleep_1(self):
        self.sleep -= 5

    def play(self):
        self.fresh -= 5
        self.sleep += 5
        self.mood += 2

    def change_move(self):
        if self.move == "покормить":
            self.eat()
        elif self.move == "помыть":
            self.wash()
        elif self.move == "усыпить":
            self.sleep_1()
        elif self.move == "поиграть":
            self.play()
        else:
            "Питомец доволен"

    def status(self):
        if self.sleep > 8:
            print("Питомец хочет спать \n")
        if self.fresh < 2:
            print("Питомец грязный \n")
        if self.feel < 3:
            print("Питомец голоден \n")
        if self.mood < 2:
            print("Питомец скучает \n")
        print("Настроение ", self.mood,
              "\nСамочувствие ", self.feel,
              "\nСвежесть ", self.fresh,
              "\nСонливость ", self.sleep)

pet1 = Pet("Tom")
while True:
    pet1.move = input("Введите действие ")
    pet1.change_move()
    pet1.status()