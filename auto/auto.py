import random


class Auto:
    speed = 2

    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def move_x(self):
        self.x += self.speed
        self.status()

    def move_y(self):
        self.y += self.speed
        self.status()


    def status(self):
        print(f"Автомобиль - x : {self.x} - y : {self.y}")


class Tracktor(Auto):
    speed = 1

    def __init__(self, name, pos):
        super().__init__(pos)
        self.name = name

    def status(self):
        print(f"{self.name} - x : {self.x} - y : {self.y}")


def main():
    tr1 = Tracktor("Camaro", (1, 1))
    for i in range(random.randrange(10)):
        tr1.move_x()
    for i in range(random.randrange(10)):
        tr1.move_y()

    tr2 = Tracktor("JJ", (1, 1))
    for i in range(random.randrange(10)):
        tr2.move_x()
    for i in range(random.randrange(10)):
        tr2.move_y()

    au = Auto((1, 1))
    for i in range(random.randrange(10)):
        au.move_x()
    for i in range(random.randrange(10)):
        au.move_y()

if __name__ == "__main__":
    main()

