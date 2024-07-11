"""
На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько
Примерно так:
букв.
2:'abc', 3:'def', 4:'gh', 5:'жки', 6:'mono', 7:'pqrs', 8:'tuv', 9:'wxyz'
Вам известно в каком порядке были нажаты клавиши телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой последовательностью
нажатий.
Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит
10 символов.
Формат вывода
Выведите все возможные комбинации букв через пробел.

Пример 1

Ввод
23

Вывод
ad ae af bd be bf cd се cf

Пример 2

Ввод
92

Вывод
wa wb wc xa xb xc ya yb yc za zb zc
"""

# Реализация получилась по времени O(4^n) и памяти O(n*4^n)

def def_combinations(n):
    alf = [(2, 'abc'),(3,'def'),(4,'ghi'),(5,'jkl'),(6,'mno'),(7,'pqrs'),(8,'tuv'),(9,'wxyz')]
    if len(n) == 1:
        return [char for char in alf[int(n[0]) - 2][1]]

    data = []
    for combination in def_combinations(n[:-1]):
        for c in alf[int(n[-1]) - 2][1]:
            data.append(combination + c)

    return data

def main():
    try:
        n = input()
        if any(int(c) < 2 or int(c) > 9 for c in n):
            raise ValueError("Invalid input for n: n must be a string of digits between 2 and 9")

        print(" ".join(map(str, def_combinations(n))))

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()