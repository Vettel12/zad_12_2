"""
Вася на уроке математики проходил степени. Он хочет написать программу, которая
определяет, будет ли положительное целое число степенью четверки.
Формат ввода
На вход подается целое число в диапазоне от 1 до 10000.
Формат вывода
True, если число является степенью четырех, False - в обратном случае.

Пример 1

Ввод
15

Вывод
False

Пример 2

Ввод
16

Вывод
True
"""

# Реализация получилась по памяти O(1), а по времени O(log(n))

def number_4(x):
    if x == 4:
        return True
    elif x % 2 != 0:
        return False
    else:
        while x % 4 == 0:
            x = x // 4
        if x == 1:
            return True
        else:
            return False

def main():
    try:
        x = int(input())
        if x < 1 or x > 10000:
            raise ValueError
        
        print(number_4(x))

    except ValueError:
        print("Invalid input")
        return
    
if __name__ == "__main__":
    main()