class Canculator:
    operations = []

    def __init__(self, a, b):
        self.a = a
        self.b = b

        if self.__check_variables():
            c = input("Введите операцию: ").lower()
            match c:
                case "сумма":
                    self.operations.append(self.print_operation(self.sum()))
                case "разность":
                    self.operations.append(self.print_operation(self.ded()))
                case "умножение":
                    self.operations.append(self.print_operation(self.mul()))
                case "деление":
                    self.operations.append(self.print_operation(self.div()))
                case _:
                    print("Такой операции не найдено. Cписок операций:\n"
                          "сумма | разность | умножение | деление")


    def sum(self):
        return [self.a + self.b, " + "]

    def ded(self):
        return [self.a - self.b, " - "]

    def mul(self):
        return [(self.a * self.b), " * "]

    def div(self):
        if self.b == 0:
            return "Нельзя делить на 0"
        else:
            return [self.a / self.b, " / "]

    def __check_variables(self):

        if not self.a.isdigit():
            try:
                self.a = float(self.a)
            except ValueError:
                print(self.a, "это не число.")
                return False
        if type(self.a) == str:
            self.a = int(a)

        if not self.b.isdigit():
            try:
                self.b = float(self.b)
            except ValueError:
                print(self.b, "это не число.")
                return False
        if type(self.b) == str:
            self.b = int(b)

        return True

    def print_operation(self, operation):
        print(self.a, operation[1], self.b, " = ", operation[0])
        return str(self.a) + operation[1] + str(self.b) + " = " + str(operation[0])

while True:
    a = input("Введите a: ")
    b = input("Введите b: ")
    can = Canculator(a, b)
    if input("\nПродолжить? ").lower() == "нет":
        break

print("\n", "Выполненные операции:", can.operations)
