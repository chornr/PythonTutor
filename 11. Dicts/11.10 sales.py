# Условие
#
# Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой
# запись вида Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар — название
# товара (строка без пробелов), количество — количество приобретенных единиц товара.
#
# Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого
# вида товаров. Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом
# порядке.

FULL = []
NAMES = []

try:
    while True:
        line = input().split()  # Get new line and convert it to list
        FULL.append(line)
        NAMES.append(line[0])
except EOFError:
    pass

NAMES = set(NAMES)
NAMES = list(NAMES)
FINALE = {}

for i in NAMES:
    FINALE[i] = []

for name in NAMES:
    for i in range(len(FULL)):
        if name in FULL[i]:
            FINALE[name].append(FULL[i][1:])

FK = list(FINALE.keys())
FK = sorted(FK)
FV = []

for key in FK:
    print(key + ":")
    FV = sorted(FINALE[key])
    D = {}
    for j in range(len(FV)):
        if not FV[j][0] in D.keys():
            D[FV[j][0]] = FV[j][1]
        else:
            D[FV[j][0]] = str(int(D[FV[j][0]]) + int(FV[j][1]))

    DK = list(D.keys())
    DK = sorted(DK)
    for k in range(len(DK)):
        tup = (DK[k], D[DK[k]])
        print(' '.join(tup))

# ChatGPT
# Неправильное решение.
# На одном из тестов ниже программа неправильно работает
from collections import defaultdict

# создаем словарь для хранения информации о покупателях и их покупках
customers = defaultdict(lambda: defaultdict(int))

# читаем данные из файла и обновляем словарь
with open('input.txt', 'r') as f:
    for line in f:
        buyer, item, quantity = line.strip().split()
        customers[buyer][item] += int(quantity)

# выводим результаты в нужном формате
for buyer in sorted(customers.keys()):
    print(buyer + ':')
    for item in sorted(customers[buyer].keys()):
        print(item, customers[buyer][item])
