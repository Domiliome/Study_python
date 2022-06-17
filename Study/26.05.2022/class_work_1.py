from abc import ABC, abstractmethod


def go(obj):
    obj.get_name()
    obj.start()
    obj.stop()


class Vehicle(ABC):

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass

    @abstractmethod
    def get_name(self): pass


class Car(Vehicle):
    type = "Легковой автомобиль"

    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"*{self.name} поехала*")

    def stop(self):
        print(f"*{self.name} остановилась*")

    def get_name(self):
        print(f"{self.name}. Тип - {self.type}.")


class Ship(Vehicle):
    type = "Корабль"

    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"*{self.name} пошёл*")

    def stop(self):
        print(f"*{self.name} остановился*")

    def get_name(self):
        print(f"{self.name}. Тип - {self.type}.")


class Helicopter(Vehicle):
    type = "Вертолёт"

    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"*{self.name} полетел*")

    def stop(self):
        print(f"*{self.name} сел*")

    def get_name(self):
        print(f"{self.name}. Тип - {self.type}.")

vehicle1 = Car("BMW")

go(vehicle1)

