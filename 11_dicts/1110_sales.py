# Условие
#
# Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой
# запись вида Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар — название
# товара (строка без пробелов), количество — количество приобретенных единиц товара.
#
# Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого
# вида товаров. Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом
# порядке.

D = {}

def inputs():
    while True:
        try:
            yield input().split()
        except (ValueError, EOFError):
            return

for name, product, amount in inputs():
    if name not in D:
        D[name] = {product: int(amount)}
    else:
        if product in D[name]:
            D[name][product] += int(amount)
        else:
            D[name][product] = int(amount)

names = list(D.keys())
names.sort()

for name in names:
    print(name + ":")
    products = list(D[name].keys())
    products.sort()
    for product in products:
        print(product + " " + str(D[name][product]))

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
