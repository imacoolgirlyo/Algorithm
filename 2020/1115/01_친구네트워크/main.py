test_case = int(input())


def find(k):
    if fr[k] != k:
        # return find(fr[k])
        p = find(fr[k])
        fr[k] = p
        return fr[k]
    else:
        return k


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        fr[b] = a
        sum_fr[a] += sum_fr[b]


for _ in range(test_case):
    n = int(input())
    fr = dict()
    sum_fr = dict()
    for i in range(n):
        a, b = list(input().split(' '))
        if a not in fr:
            fr[a] = a
            sum_fr[a] = 1
        if b not in fr:
            fr[b] = b
            sum_fr[b] = 1

        union(a, b)
        print(sum_fr[find(a)])
