# Полиморфизм
class Car():
    @staticmethod
    def execute(o):
        o.start()
        o.signal()
        o.stop()


class Audi(Car):

    def move(self):
        print("Поехали")

    def start(self):
        print("Audi start")

    def stop(self):
        print("Audi stop")

    def signal(self):
        print("*bip bup*")


car1 = Audi()
Car.execute(car1)
