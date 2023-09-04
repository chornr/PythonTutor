# Условие
# Даны два элемента в дереве. Определите, является ли один из них потомком другого.
#
# Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K. В каждой из следующих K строк, содержатся имена двух элементов дерева.
#
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если второй является предком первого или 0, если ни один из них не является предком другого.

# CORRECT
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
            
m = int(input())
results = []

for i in range(m):
    name_1, name_2 = input().split()
    height = family_tree[name_1] - family_tree[name_2]
        
    if height < 0:
        while height < 0:
            name_2 = family[name_2]
            height = height + 1
        if name_2 == name_1:
            results.append("1")
        else:
            results.append("0")

    elif height > 0:
        while height > 0:
            name_1 = family[name_1]
            height = height - 1
        if name_1 == name_2:
            results.append("2")
        else:
            results.append("0")
    
    else:
        results.append("0")

print(" ".join(results))


# NOT COMPLETED
def dicts_genealogy_ancestors_and_descendants():
    N = int(input())
    PARENTS = []
    KIDS = []

    # Create two lists - kids and parents
    for i in range(N - 1):
        young, old = input().split()
        PARENTS.append(old)
        KIDS.append(young)

    M = int(input())
    L = []
    F = []

    for i in range(M):
        one, two = input().split()
        L.append((one, two))

        if one in KIDS and two in PARENTS:
            low = one
            high = None
            for j in range(len(KIDS)):
                high = PARENTS[KIDS.index(low)]
                if high in KIDS:
                    low = high
                    high


        elif one in PARENTS and two in KIDS:

        else:
            print(0)
