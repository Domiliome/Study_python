"""
О том как работает *args и *kwargs
Такая запись придаёт гибкость программе
"""


# создаётся кортеж args с аргументами
def print_args(*args):
    args = list(args)
    for i in range(len(args)):
        print(f"{i + 1}-й аргумент: {args[i]}")


# создаётся словарь kwargs c названиями и значениями аргументов
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"Значение для {key} является {value}")


print_args(0, 2, 3)
print_kwargs(name="Sammy", your_name="Casey")
