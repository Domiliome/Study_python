class ControlList:

    @staticmethod
    def average(a):
        return sum(a) / len(a)

    @staticmethod
    def zerozero(arr):
        for i, x in enumerate(arr):
            if x == 0 and i != len(arr) - 1:
                if a[i + 1] == 0:
                    print(f"Два нуля в индексах {i}, {i + 1}")
        print(ControlList.average(arr))

    @staticmethod
    def division_num(arr, num):
        left = []
        right = []
        for thing in arr:
            if thing < num:
                right.append(thing)
            else:
                left.append(thing)
        return left, right

    @staticmethod
    def sum_elementary_num(num):
        i = num
        a = []
        while i >= 1:
            a.append(i % 10)
            i = i // 10
            print(a)
        return sum(a)

    @staticmethod
    def fact(a):
        if a == 0:
            return 1
        return a * ControlList.fact(a - 1)

    @staticmethod
    def wfact(a):
        i = a
        result = 1
        while i > 0:
            result *= i
            i -= 1
        return result


print(ControlList.fact(997))
print(ControlList.wfact(12))
