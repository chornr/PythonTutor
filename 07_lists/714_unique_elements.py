# coding=utf-8 Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно
# выводить в том порядке, в котором они встречаются в списке.

from typing import List

L = [int(i) for i in input().split()]  # type: List[int]
count = 0

for i in range(len(L)):
    for j in range(i+1, len(L)):
        if L[i] == L[j]:
            count += 1
print(count)
