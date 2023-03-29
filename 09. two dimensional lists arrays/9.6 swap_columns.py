# coding=utf-8
# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат. Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j).

n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]

def swap_columns(a, i, j):
    # type: (object, object, object) -> object
    rotated = list(zip(*a[::-1]))  # Python 3

    if i < j:
        el = rotated[i]
        rotated[i] = rotated[j]
        rotated[j] = el
    else:
        el = rotated[j]
        rotated[j] = rotated[i]
        rotated[i] = el

    rotated = list(zip(*rotated[::-1]))  # Python 3
    rotated = list(zip(*rotated[::-1]))  # Python 3
    rotated = list(zip(*rotated[::-1]))  # Python 3

    for row in rotated:
        for elem in row:
            print(elem, end=' ')
        print()


swap_columns(a, i, j)
