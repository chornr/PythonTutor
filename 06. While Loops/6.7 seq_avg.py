# coding=utf-8
# Определите среднее значение всех элементов последовательности, завершающейся числом 0.

n = int(input())
count = 0
L = []

while n != 0:
    L.append(n)
    count += 1
    n = int(input())

print(sum(L) / (count))
