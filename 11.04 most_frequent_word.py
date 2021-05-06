# Условие
#
# Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом
# тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

n = int(input())
D = dict()

for i in range(n):
    row = input().split()
    for word in row:
        D[word] = D.get(word, 0) + 1

for key in sorted(D):
    if D[key] == max(D.values()):
        print(key)
        break
