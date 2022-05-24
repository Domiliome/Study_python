from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def move(self): pass


class Audi(Car):

    def move(self):
        print("Поехали")


car1 = Audi()
car1.move()
