# coding=utf-8
# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих
# элементов этой последовательности равны друг другу.

n = int(input())
L = []

while n != 0:
    L.append(n)
    n = int(input())

count = 1
countmax = 1
for i in range(1, len(L)):
    prev = L[i - 1]
    cur = L[i]
    if prev == cur:
        count += 1
    else:
        if count > countmax:
            countmax = count
        count = 1
print(max(countmax, count))
