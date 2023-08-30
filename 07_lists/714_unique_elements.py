# coding=utf-8 Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

L = [int(i) for i in input().split()]
L1 = []

for element in L:
    if L.count(element) == 1:
        L1.append(str(element))

print(" ".join(L1))
