from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def say_name(self): pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"Собаку зовут {self.name}")


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"Кошку зовут {self.name}")


myDog = Cat("meow")
myDog.say_name()
