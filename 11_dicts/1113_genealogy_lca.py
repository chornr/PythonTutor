# Условие
#
# В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common
# Ancestor). Наименьшим общим предком элементов A и B является такой элемент C, что С является предком A, C является
# предком B, при этом глубина C является наибольшей из возможных. При этом элемент считается своим собственным предком.
#
# Формат входных данных аналогичен предыдущей задаче
#
# Для каждого запроса выведите наименьшего общего предка данных элементов.

# RESOLUTION 1
n = int(input())
family = dict()
family_tree = dict()

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
            
def find_ancestors(name1, name2):
    ancestors = []
    for _ in range(family_tree[name1]+1):
        ancestors.append(name1)
        try:
            name1 = family[name1]
        except KeyError:
            break
            
    for _ in range(family_tree[name2]+1):
        if name2 in ancestors:
            return name2
        else:
            name2 = family[name2]

m = int(input())
results = []

for _ in range(m):
    name_1, name_2 = input().split()
    print(find_ancestors(name_1, name_2))

# RESOLUTION 2

n = int(input())
family = dict()

for i in range(n-1):
    kid, parent = input().split()
    family[kid] = parent
            
def find_ancestors(name1, name2):
    ancestors = []
    status = True
    while status is True:
        ancestors.append(name1)
        try:
            name1 = family[name1]
        except KeyError:
            status = False
    status = True
    while status is True:
        if name2 in ancestors:
            return name2
        else:
            try:
                name2 = family[name2]
            except KeyError:
                status = False

m = int(input())
for _ in range(m):
    name_1, name_2 = input().split()
    print(find_ancestors(name_1, name_2))

# RESOLUTION 3

def find_ancestors(name1, name2):
    ancestors = []
    while True:
        ancestors.append(name1)
        try:
            name1 = family[name1]
        except KeyError:
            break
    while True:
        if name2 in ancestors:
            return name2
        else:
            try:
                name2 = family[name2]
            except KeyError:
                break

n = int(input())
family = dict()
for i in range(n-1):
    kid, parent = input().split()
    family[kid] = parent

m = int(input())
for _ in range(m):
    name_1, name_2 = input().split()
    print(find_ancestors(name_1, name_2))
