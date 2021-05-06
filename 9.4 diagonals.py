# coding=utf-8
# Условие Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали
# должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях
# числа 2, и т.д.

n = int(input())
L = []

for i in range(n):
    N = []
    L.append(N)
    for j in range(n):
        N.append(abs(i - j))

for row in L:
    for elem in row:
        print(elem, end=' ')
    print()