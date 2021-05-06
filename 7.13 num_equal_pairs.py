# coding=utf-8
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.

L = [int(i) for i in input().split()]
count = 0

for i in range(len(L)):
    for j in range(i+1, len(L)):
        if L[i] == L[j]:
            count += 1
print(count)
