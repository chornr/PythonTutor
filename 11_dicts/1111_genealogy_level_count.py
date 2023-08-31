# Условие
#
# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
#
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота
# равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
#
# Вам дано генеалогическое древо, определите высоту всех его элементов.
#
# Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя
# для каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
#
# Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого
# элемента необходимо вывести его высоту.
#
# Примечание
#
# Эта задача имеет решение сложности O(n), но вам достаточно написать решение сложности O(n2) (не считая сложности
# обращения к элементам словаря).

# LATEST RESOLUTION
n = int(input())
family = {}
family_tree = {}
for i in range(n-1):
    kid, parent = input().split()
    family[kid] = parent
while len(family_tree) != n:
    for kid, parent in family.items():
        if parent not in family.keys():
            family_tree[parent] = 0
            family_tree[kid] = 1
        elif parent in family_tree:
            family_tree[kid] = family_tree[parent] + 1
parents = list(family_tree.keys())
parents.sort()
for name in parents:
    print(name, family_tree[name])

# OLD RESOLUTION
def dict_genealogy_levels():
    N = int(input())
    PARENTS = []
    KIDS = []

    # Create two lists - kids and parents
    for i in range(N - 1):
        young, old = input().split()
        KIDS.append(young)
        PARENTS.append(old)

    # find out Grandfather
    grand = list(set(PARENTS) - set(KIDS))[0]

    # final Dict with hierarchy
    LEVELS = {grand: 0}

    # new list of Parents. Will be extended with new Fathers as they discovered
    New = [grand]

    for i in range(N):
        for kid in KIDS:
            if PARENTS[KIDS.index(kid)] == grand:
                LEVELS[kid] = LEVELS[grand] + 1
                New.append(kid)
        ind = New.index(grand) + 1
        if ind != len(KIDS):
            grand = New[ind]

    NAMES = list(LEVELS.keys())
    NAMES.sort()

    for i in NAMES:
        print(i, LEVELS[i])


# ChatGPT
# Неправильное решение.
# На одном из тестов ниже программа неправильно работает
def dfs(node, height, parents, heights):
    """
    Функция для выполнения DFS на дереве
    """
    heights[node] = height
    if node in parents:
        parent = parents[node]
        dfs(parent, height+1, parents, heights)


# Чтение входных данных
n = int(input())
parents = {}
for i in range(n-1):
    child, parent = input().split()
    parents[child] = parent

# Вычисление высоты каждого элемента
heights = {}
for node in parents.keys():
    dfs(node, 0, parents, heights)

# Формирование и сортировка списка элементов
elements = [(node, heights[node]) for node in set(parents.keys()) | set(parents.values())]
elements.sort()

# Вывод элементов
for element in elements:
    print(element[0], element[1])
