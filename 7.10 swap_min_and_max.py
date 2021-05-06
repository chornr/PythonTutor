# coding=utf-8
# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

L = [int(i) for i in input().split()]
a = min(L)
b = max(L)

if L.index(a) < L.index(b):
    L[L.index(b)] = a
    L[L.index(a)] = b
else:
    L[L.index(a)] = b
    L[L.index(b)] = a

print(' '.join([str(i) for i in L]))
