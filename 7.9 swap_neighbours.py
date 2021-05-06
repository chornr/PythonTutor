# coding=utf-8
# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число,
# то последний элемент остается на своем месте.

L = [int(i) for i in input().split()]
L1 = L[1::2]
L2 = L[0::2]
L3 = []

for i in range(max(len(L1), len(L2))):
    if i <= (len(L1) - 1):
        L3.append(L1[i])
    if i <= (len(L2) - 1):
        L3.append(L2[i])

print(' '.join([str(i) for i in L3]))
