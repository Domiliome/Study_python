import re

NUMBER = {'data_type': 'Номер',
          'sample': '+7123456789',
          'regexp': r"\+[\d+]{11}"}

EMAIL = {'data_type': 'E-MAIL',
         'sample': 'google@gmail.com',
         'regexp': r"[\w'._+-]+@[\w'._+-]+"}


def verification(pattern):
    while True:
        print(f"Шаблон {pattern['sample']}")
        data = input(f"Введите {pattern['data_type']}:")
        if not re.fullmatch(pattern["regexp"], data):
            print(f"Некорректый {pattern['data_type']}\n")
            continue
        return data


a = verification(EMAIL)

print(a)


i = {'name': 'vova', 'message': "hello", 'datatime': '20.12.2020'}

print(f"{i['datatime']} {i['name']} {i['message']})