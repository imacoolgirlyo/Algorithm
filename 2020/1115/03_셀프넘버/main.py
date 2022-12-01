not_self_set = set()

for i in range(1, 10001):
    result = i
    for j in str(i):
        result += int(j)
    not_self_set.add(result)

self_set = set(range(1, 10001)) - not_self_set
self_list = sorted(list(self_set))
for i in self_list:
    print(i)
