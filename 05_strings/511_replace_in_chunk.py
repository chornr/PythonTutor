# coding=utf-8
# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

s = input()

s1 = s[0:s.find('h')+1]
s2 = s[s.find('h')+1:s.rfind('h')].replace('h','H')
s3 = s[s.rfind('h')::]

print(s1 + s2 + s3)
