"""
А теперь помогите Васе решить задачу по информатике. Он снова томится дома в хорошую
погоду.
На вход подается строка длиной от 1 до 10000 символов. Нужно отсортировать её в порядке
частот букв по встречаемости. Заглавные и строчные буквы считаются разными. Если частота
одинаковая, нужно применить вторичную сортировку лексикографически.
Формат ввода
Одна строка длиной не более 10000 символов.
Формат вывода
Строка, в которой символы отсортированы в порядке убывания частотности.

Пример 1

Ввод
tree
Вывод
eert

Пример 2

Ввод
ztwidhfk
Вывод
dfhiktwz
"""

# Реализация получилась по памяти O(n), а по времени O(n^2)

def freq(string):
    char_count = {}
    for x in string:
        if x not in char_count:
            char_count[x] = 1
        else:
            char_count[x] += 1
    char_list = list(char_count.items())
    result = []
    for x in range(len(char_list)-1):
        for y in range(x+1, len(char_list)):
            if (char_list[x][1] < char_list[y][1]) or ((char_list[x][0] > char_list[y][0]) and (char_list[x][1] == char_list[y][1])):
                char_list[x], char_list[y] = char_list[y], char_list[x]

    for char, count in char_list:
        result += char * count
    return result

def main():
    try:
        string = input()
        if len(string) > 10000:
            raise ValueError ("Invalid input for string: string must be a string of length less than 10000")

        print("".join(map(str, freq(string))))

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()