class Calculator:
    results = []
    number_1 = 0
    number_2 = 0
    operation = "+"

    def plus(self):
        return self.number_1 + self.number_2

    def minus(self):
        return self.number_1 - self.number_2

    def mult(self):
        return self.number_1 * self.number_2

    def div(self):
        try:
            return self.number_1 / self.number_2
        except ZeroDivisionError:
            print("Деление на 0")
    def calculate(self):

        if self.__prepareData():
            if self.operation == "+":
                result = self.plus()
            elif self.operation == "-":
                result = self.minus()
            elif self.operation == "*":
                result = self.mult()
            elif self.operation == "/":
                result = self.div()
            else:
                return False
            return result
        else:
            return "Введены не числа"

    def __prepareData(self):
        try:
            self.number_1 = float(self.number_1)
            self.number_2 = float(self.number_2)
            return True
        except ValueError:
            return False

    def print_result(self, result):
        resultStr = f"{self.number_1} {self.operation} {self.number_2}"
        self.results.append(resultStr)

calc = Calculator()
while True:
    calc.number_1 = input("Введите первое число:")
    calc.number_2 = input("Введите второе число:")
    calc.operation = input("Введите операцию:")
    print(calc.calculate())