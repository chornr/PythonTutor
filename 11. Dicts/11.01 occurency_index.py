# Условие
# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно
# встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.

# My solution
counter = {}  # инициализируем пустой словарь
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')

# ChatGPT solution
text = input() # вводим текст как одну строку
word_count = {} # инициализируем пустой словарь
words = text.split() # разбиваем строку на слова
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 0
    print(word_count[word], end=" ")
