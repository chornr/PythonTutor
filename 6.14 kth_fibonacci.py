# coding=utf-8
# Последовательность Фибоначчи определяется так:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# По данному числу n определите n-е число Фибоначчи φn.
#
# Эту задачу можно решать и циклом for.

F0 = 0
F1 = 1
F2 = 1
n = int(input())
m = 1

if n <= F2:
    print(n)
else:
    while m != n:
        F2 = F0 + F1
        F0 = F1
        F1 = F2
        m = m + 1
    print(F2)