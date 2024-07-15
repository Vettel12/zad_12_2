"""
Руководство компании, где работают Гоша с друзьями, подарило каждому сотруднику два
талона на обед в близлежащем ресторане. Сотрудники могли взять талоны и записать номер
своего бейджика в специальный бланк. Так сделали все кроме одного сотрудника, он мог
вести себя только 1 раз, или же число его записей больше двух. Нужно вычислить, кто же это
такой! На вход подается непустой массив целых чисел. Каждое из них, за исключением одного,
встречается 2 раза. Размер массива не превосходит 10000. Числа по модулю не больше
10000. Нужно выяснить, кто не такой, как все!
Формат ввода
В первой строке записано число n. Во второй строке через пробел записаны чисел. Длина
массива и каждое из чисел не превосходят 10000.

Формат вывода
Выведите единственное число, соответствующее id отличившегося сотрудника

Пример 1

Ввод
5
4 1 2 1 2

Вывод
4

Пример 2

Ввод
5
42 67 67 42 42

Вывод
42
"""
# Реализация получилась по памяти O(n), а по времени O(n)

def breakfast(n, number):
    num = {}
    for x in range(n):
        if number[x] not in num:
            num[number[x]] = 1
        else:
            del num[number[x]]
    return list(num.keys())[0]

def main():
    try:
        n = int(input())
        number = list(map(int, input().split()))
        if n > 10000:
            raise ValueError("Invalid input for n: n must be an integer between 1 and 10000")
        if len(number) != n:
            raise ValueError("Invalid input for number: number must be a list of length n")
        for x in number:
            if abs(x) < 1 or abs(x) > 10000:
                raise ValueError("Invalid input for number: numbers must be integers between 1 and 10000")
        print(breakfast(n, number))
    except ValueError:
        print("Invalid input") 


if __name__ == "__main__":
    main()