from datetime import date
from dateutil.relativedelta import relativedelta

PRICE = 400 # задолжность за месяц

file = open("/home/eugene/Документы/users.csv", "r")
arr = file.read().split("\n")
file.close()

for i in range(len(arr)):
    arr[i] = arr[i].split(",")

arr = arr[:-1]
for i in range(len(arr)):
    print(i)
    arr_result = [f"Справка по лицевому счёту №{arr[i][1]}",
                  "\nФИО", "Адрес",
                  f"\n{arr[i][0]}", arr[i][2],
                  "\nТаблица"]

    duty = 0
    for j in range(int(arr[i][3])):
        duty += PRICE
        arr_result.extend([f"\n {date.today() + relativedelta(months=-(int(arr[i][3]) - j))}", f"{duty} руб"])
    arr_result.extend(["\n Итого", f"{duty} руб"])

    result = open(f"/home/eugene/Документы/{arr[i][0]}.csv", "w")
    result.write(",".join(arr_result))
    result.close()
