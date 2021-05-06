# coding=utf-8
# Дано натуральное число. Найдите число десятков в его десятичной записи.

a = int(input())

if a > 9:
    print(int(str(a)[-2]))
else:
    print(0)
