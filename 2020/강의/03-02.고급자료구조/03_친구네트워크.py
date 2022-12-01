def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        network[x] += network[y]


test_case = int(input())

for _ in range(test_case):
    parent = dict()
    network = dict()
    f = int(input())
    for i in range(f):
        x, y = input().split(' ')
        if x not in parent:
            parent[x] = x
            network[x] = 1
        if y not in parent:
            parent[y] = y
            network[y] = 1
        union(x, y)
        print(network[find(x)])
