from heapq import heappop, heappush
n, m = map(int, input().split())

info = [[] for i in range(n+1)]
indegree = [0]*(n+1)

heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    info[x].append(y)
    indegree[y] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heappush(heap, i)

while heap:
    data = heappop(heap)
    result.append(data)
    for y in info[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heappush(heap, y)

for i in result:
    print(i, end=' ')
