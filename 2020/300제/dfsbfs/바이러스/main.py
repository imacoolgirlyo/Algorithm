from collections import deque

n, m = int(input()), int(input())
node_info = [[] for _ in range(n+1)]
visited = [0]*(n+1)
result = 0

for _ in range(m):
    x, y = map(int, input().split())
    node_info[x].append(y)
    node_info[y].append(x)

q = deque([1])
visited[1] = 1

while q:
    v = q.popleft()
    result += 1

    for i in node_info[v]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)


print(result-1)
