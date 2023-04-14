# coding=utf-8
# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.

import math
a = int(input())
b = int(input())

print(math.sqrt(a*a+b*b))