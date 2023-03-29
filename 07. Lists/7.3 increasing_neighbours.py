# coding=utf-8
# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

L = input().split()  # type: object

for i in range(1, len(L)):
    if int(L[i]) > int(L[i-1]): print(L[i])