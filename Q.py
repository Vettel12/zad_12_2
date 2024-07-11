"""
В метро Гоша обычно играет в мобильную игру «Черепашенька». Он долго собирал данные о
том, сколько очков зарабатывает и проигрывает в день. Гоша собирает необычную статистику.
Нужно определить максимальное произведение заработанных очков среди троек дней, в
которые сумма очков равна нулю, и произведение является положительным числом.
Формат ввода
В первой строке записано число n (1 Sn 2000). В следующей строке через пробел
n целых чисел. Числа находятся в диапазоне от -10000 до 10000.
записаны
Формат вывода
Выведите максимальное положительное произведение заработанных за три дня очков среди
троек дней, в которые их сумма равна нулю. Если троек, удовлетворяющих условиям, нет,
нужно вывести -1.

Пример 1

Ввод
5
-2 -1 3 -1 -2

Вывод
6

Пример 2

Ввод
5
-2 1 1 -1 -2

Вывод
-1

Примечания
Решение должно использовать O(1) дополнительной памяти (помимо массива, в который
считаны входные данные).
"""

# Реализая получилась по памяти O(1), а по времени O(n^2)

def stat(n, number):
    number = sorted(number)
    max_product = -1
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            if number[i] + number[left] + number[right] == 0:
                if number[i] * number[left] * number[right] > max_product:
                    max_product = number[i] * number[left] * number[right]
                left += 1
                right -= 1
            elif number[i] + number[left] + number[right] < 0:
                left += 1
            else:
                right -= 1
    return max_product
    
def main():
    try:
        n = int(input("Введите количество чисел n: "))
        if not isinstance(n, int) or n < 1 or n > 2000:
            raise ValueError("Invalid input for n: n must be an integer between 1 and 2000")

        number = list(map(int, input("Введите список целых чисел: ").split()))
        if len(number) != n:
            raise ValueError(f"Invalid input for number list: length must be equal to n ({n})")

        for num in number:
            if not isinstance(num, int) or num < -10000 or num > 10000:
                raise ValueError("Invalid input for number list: numbers must be integers between -10000 and 10000")

        print(stat(n, number))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()