# Условие
# Даны два элемента в дереве. Определите, является ли один из них потомком другого.
#
# Во входных данных записано дерево в том же формате, что и в предыдущей задаче Далее идет число запросов K. В каждой из следующих K строк, содержатся имена двух элементов дерева.
#
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если второй является предком первого или 0, если ни один из них не является предком другого.

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