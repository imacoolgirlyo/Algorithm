from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]


def dfs(x):
    visited[x] = True
    print(x, end=' ')

    for d in graph[x]:
        if visited[d] == False:
            dfs(d)


def bfs(x):
    q = deque([x])
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for i in graph[v]:
                if not visited[i]:
                    q.append(i)


for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)
