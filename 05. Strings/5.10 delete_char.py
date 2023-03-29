# coding=utf-8
# Дана строка. Удалите из этой строки все символы @.

s1 = input()
s2 = ''

for i in s1:
    if i != '@':
        s2 += i
print(s2)
