from Behavior.FlyWithWings import FlyWithWings
from Duck.Duck import Duck


class RubberDuck(Duck):
    def __init__(self, name):
        super().__init__(name)
        print(super(self.fly_behavior))
    def display(self):
        print("Rubber Duck")


class RedDuck(Duck, FlyWithWings):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print("Red Duck")
