"""
Тимофей собирает метрики посещаемости сайта за последний месяц с двух серверов. На
каждой машине имеется список id пользователей, отсортированный в порядке от
минимального количества посещений к максимальному, вам известно число посещений
каждого пользователя. Пользователи, не посещавшие сайт в последний месяц, не
учитываются. Вам нужно сделать общий список числа посещений для двух серверов так.
чтобы в нем тоже числа шли по возрастанию. Так как сайт Тимофея очень популярен, то
данных о пользователях много, поэтому Тимофей может позволить себе только линейное
время работы алгоритма.
Формат ввода
В первой строке записаны количества посещений пользователей с первого сервера через
пробел, в конце - k нулей. Во второй строке записано число - количество пользователей,
пришедших с первого сервера (без учета нулей в конце списка). В третьей - число k - которое,
помимо количества нулей, также является длиной списка пользователей со второго сервера. В
последней строке - список посещений со второго сервера (k штук).
Количество посещений каждого пользователя не превосходит 10000, числа т и к также не
превосходят 10000
Формат вывода
В одной строке через пробел выведите элементы получившегося списка в отсортированном
порядке.

Пример 1

Ввод
1 2 3 0 0 0
3
3
2 5 6

Вывод
1 2 2 3 5 6

Пример 2

Ввод
8 98 0
2
1
65

Вывод
8 65 98

Примечания
Дополнительную память использовать нельзя, все id нужно сохранять в первом массиве.
"""

# Реализация получилась по памяти O(1), а по времени O(n^2)

def vasya(first_server, m, k, second_server):
    first_server = first_server[:m]
    first_server = first_server + second_server
    for x in range(len(first_server)-1):
        for y in range(x+1, len(first_server)):
            if first_server[x] > first_server[y]:
                first_server[x], first_server[y] = first_server[y], first_server[x]
    return first_server

def main():
    try:
        first_server = list(map(int, input().split()))
        m = int(input())
        k = int(input())
        second_server = list(map(int, input().split()))
        if len(first_server) > 10000:
            raise ValueError ("Invalid input for first_server: first_server must be a list of integers less than 10000")
        if len(second_server) > 10000:
            raise ValueError ("Invalid input for second_server: second_server must be a list of integers less than 10000")
        if k > 10000:
            raise ValueError ("Invalid input for k: k must be an integer less than 10000")
        if m > 10000:
            raise ValueError ("Invalid input for m: m must be an integer less than 10000")
        
        print(" ".join(map(str, vasya(first_server, m, k, second_server))))

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()