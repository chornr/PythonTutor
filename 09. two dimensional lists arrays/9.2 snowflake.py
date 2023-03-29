# coding=utf-8
# Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент
# массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец
# массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение
# звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.

n = int(input())
L = [['.' for i in range(n)] for i in range(n)]

# vertical replacement
for el in L:
    el[n // 2] = '*'

# horizontal
for i in range(n):
    L[n // 2][i] = '*'

# diag
left = 0
right = n - 1
for el in L:
    for i in range(n):
        if i == left or i == right:
            el[i] = '*'
    left += 1
    right -= 1

for row in L:
    for elem in row:
        print(elem, end=' ')
    print()