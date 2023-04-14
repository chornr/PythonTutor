# coding=utf-8
# Условие Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в
# шахматном порядке. В левом верхнем углу должна стоять точка.

n, m = [int(i) for i in input().split()]

L = []

for i in range(n):
    L.append([])
    for j in range(m):
        if ((i % 2) + (j % 2)) % 2 == 0:
            L[i].append('.')
        else:
            L[i].append('*')

for row in L:
    for elem in row:
        print(elem, end=' ')
    print()