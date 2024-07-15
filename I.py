"""
Тимофей спросил у студента Саши, умеет ли тот работать с числами в двоичной системе
счисления. Он ответил, что проходил это на одной из первых лекций по информатике.
Тимофей предложил Саше решить задачку. Два числа записаны в двоичной системе
счисления. Нужно вывести их сумму, также в двоичной системе. Встроенную в язык
программирования возможность сложения двоичных чисел применять нельзя.
Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа
не превосходит 10000 цифр.
Формат вывода
Одно число в двоичной системе счисления.

Пример 1

Ввод

Вывод
1010
1011

Пример 2
10101

Ввод
1
1

Вывод
10

Примечания
Решение должно работать за O(N) и использовать O(N) дополнительной памяти,
количество разрядов максимального числа на входе.
где N -
"""

# Реализация получилась по памяти O(n), а по времени O(n)

def two_bin(a, b):
    sum = []
    temp = 0
    for x in range(len(a)):
        c = int(a[len(a)-1-x]) + int(b[len(a)-1-x])
        if c != 2 and temp == 0:
            sum.insert(0,c)
        elif x != len(a)-1 and x == 0:
            sum.insert(0,0)
            temp = 1
        elif x != len(a)-1 and c == 2:
            sum.insert(0,temp)
            temp = 1
        elif x != len(a)-1 and c != 2:
            sum.insert(0,1)
            temp = 0
        else:
            sum.insert(0,temp)
            sum.insert(0,1)
    return sum


def main():
    try:
        a = input()
        b = input()
        if len(a)>10000:
            raise ValueError ("Invalid input for a: a must be a string of length less than 10000")
        if len(b)>10000:
            raise ValueError ("Invalid input for b: b must be a string of length less than 10000")
        print("".join(map(str, two_bin(a,b))))
    except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()