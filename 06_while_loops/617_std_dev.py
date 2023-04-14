# coding=utf-8
# Дана последовательность натуральных чисел x1, x2, ..., xn. Стандартным отклонением называется величина
# σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√
# где s=x1+x2+…+xnn — среднее арифметическое последовательности.
#
# Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.

from math import sqrt
L = []
while True:
    n = int(input()) 
    if n == 0: break
    else: L.append(n)

s = sum(L) / len(L)

numerator = 0  # type: int
for element in L: numerator = numerator + (element - s)**2

print(sqrt(numerator / (len(L)-1)))