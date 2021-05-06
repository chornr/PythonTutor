# coding=utf-8
# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние
# между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции. Если
# вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе теорему Пифагора. Попробуйте прочитать о 
# ней на Википедии. 

from math import sqrt


def distance(x1, y1, x2, y2):
    # type: (object, object, object, object) -> object
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    c = sqrt(a ** 2 + b ** 2)
    return c


x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))
