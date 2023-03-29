# coding=utf-8
# Определите количество четных элементов в последовательности, завершающейся числом 0.

n = int(input())
count = 0

while n != 0:
    if n % 2 == 0:
        count += 1
    n = int(input())

print(count)