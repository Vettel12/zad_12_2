"""
Алла писала код, добавляющий запись в новую таблицу базы данных. И вдруг получила
ошибку duplicate foreign key constraint. В тот же момент её отвлекла Рита. Алла случайно
закрыла окно терминала с информацией о том, какое именно значение стало причиной
ошибки. Зато у неё сохранился список id, использованных при запросе. Помогите ей выяснить,
какой id стал причиной ошибки.
Дан массив чисел, состоящий из п целых чисел. Одно число встречается более одного раза.
Нужно определить это число.
Формат ввода
В первой строке записано число п, которое не превосходит 1000. В следующей строке
пробел записаны п целых чисел, каждое из которых также не превосходит 10000.
через
Формат вывода
Выведите одно число.

Пример 1

Ввод
5
3 1 3 4 2

Вывод
3

Пример 2

Ввод
3
2 8 8

Вывод
8
"""

# # Реализация получилась по памяти O(n), а по времени O(n)

def base_data(n, number):
    freq_number = {}
    for x in range(n):
        if number[x] not in freq_number:
            freq_number[number[x]] = 1
        else:
            number = number[x]
            break
    return number

def main():
    try:
        n = int(input("Введите количество чисел n: "))
        number = list(map(int, input("Введите список чисел: ").split()))
    
        if not isinstance(n, int) or n < 1 or n > 1000:
            raise ValueError("Invalid input for n: n must be an integer between 1 and 1000")
        if not isinstance(number, list) or len(number) < 1 or len(number) > 1000:
            raise ValueError("Invalid input for number: number must be a list of length between 1 and 1000")
        for i in range(len(number)):
            if not isinstance(number[i], int) or number[i] < 1 or number[i] > 10000:
                raise ValueError("Invalid input for number: number must be a list of integers between 1 and 10000")

        print(base_data(n, number))

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()