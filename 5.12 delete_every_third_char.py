# coding=utf-8
# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

s = input()
l = len(s)
s1 = ''
ind = 0

for i in range(len(s)):
    if i % 3 != 0:
        s1 = s1 + s[i]

print(s1)
