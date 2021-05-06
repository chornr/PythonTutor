# coding=utf-8
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

n = int(input())
sum = 0
prod = 1
s = ''

for i in range(1, n + 1):
    s = s + str(i)
    print(s)
