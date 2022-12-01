n, m = list(map(int, input().split(' ')))
parent = dict()


def find(x):
    if parent[x] != x:
        p = find(parent[x])
        parent[x] = p
        return parent[x]
    else:
        return x


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


for _ in range(m):
    k, a, b = list(map(int, input().split(' ')))

    if a not in parent:
        parent[a] = a
    if b not in parent:
        parent[b] = b

    if k == 0:
        union(a, b)
    else:
        a = find(a)
        b = find(b)
        if a != b:
            print('NO')
        else:
            print('YES')
