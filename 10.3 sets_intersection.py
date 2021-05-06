# coding=utf-8
# Условие
# Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
# Примечание. И даже эту задачу на Питоне можно решить в одну строчку.

print(*sorted(set(input().split()) & set(input().split()), key=int))


# print(' '.join([str(i) for i in sorted(list(set([int(i) for i in input().split()]) & set([int(i) for i in input().split()])))]))



# A = set(input().split())
# B = set(input().split())
# C = list(A & B)
# print(' '.join([str(i) for i in sorted(C)]))