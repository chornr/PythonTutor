# Условие
# Дан список стран и городов каждой страны. Затем даны названия городов. 
# Для каждого города укажите, в какой стране он находится.

n = int(input()) # number of countries
D = dict()

for i in range(n):
    countries = input().split()
    D[countries[0]] = countries[1::]

m = int(input()) # number of cities
for i in range(m):
    city = input()
    for country in D.keys():
        if city in D[country]:
            print(country)

# 2
# USA Boston Pittsburgh Washington Seattle
# UK London Edinburgh Cardiff Belfast
# 3
# Cardiff
# Seattle
# London


# ChatGPT

# Считываем список стран и городов
n = int(input())  # количество стран
countries = {}    # словарь со списками городов для каждой страны
for i in range(n):
    line = input().split()
    country = line[0]
    cities = line[1:]
    countries[country] = cities

# Находим страну для каждого города
m = int(input())  # количество городов для поиска
for i in range(m):
    city = input().strip()
    for country, cities in countries.items():
        if city in cities:
            print(country)
            break
