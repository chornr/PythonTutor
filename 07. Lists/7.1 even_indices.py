# coding=utf-8
# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

L = input().split()
M = []
for i in range(len(L)):
    if i % 2 == 0:
        M.append(L[i])
print(' '.join(M))
