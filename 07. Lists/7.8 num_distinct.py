# coding=utf-8
# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

L = [int(i) for i in input().split()]

N = []

for element in L:
    if element not in N:
        N.append(element)

print(len(N))
