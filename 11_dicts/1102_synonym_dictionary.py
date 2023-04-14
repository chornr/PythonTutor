# Условие
# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.


# My code
D = dict()

for i in range(int(input())):
    row = input().split()
    D[row[0]] = row[1]
    D[row[1]] = row[0]

print(D[input()])


# ChatGPT
n = int(input()) # количество пар слов в словаре

synonyms = {} # создаем пустой словарь синонимов

for i in range(n):
    word1, word2 = input().split() # считываем очередную пару слов
    synonyms[word1] = word2 # добавляем пару в словарь
    synonyms[word2] = word1 # добавляем обратную пару в словарь

last_word = input() # считываем последнее слово

synonym = synonyms[last_word] # находим синоним последнего слова

print(synonym) # выводим синоним
