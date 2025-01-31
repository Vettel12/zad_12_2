"""
Васе очень понравилась задача про анаграммы и он придумал к ней модификацию. Есть 2
строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием букв
строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.
Формат ввода
На вход подаются строки s и t, разделенные переносом строки.
Формат вывода
Выведите лишнюю букву.

Пример 1

Ввод
abcd
abcde

Вывод
e

Пример 2

Ввод
go
ogg

Вывод
g

Пример 3

Ввод
xtkpx
xkctpx

Вывод
c
"""

# Реализация получилась по памяти O(1), а по времени O(n)

def bukva(str1, str2):
    for x in range(len(str2)):
        if str2[x] in str1:
            str1 = str1.replace(str2[x], "", 1)
        else:
            return str2[x]
            
def main():
    str1 = input()
    str2 = input()

    print(bukva(str1, str2))

if __name__ == "__main__":
    main()