from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

max_value = -1

for i in range(1, n+1):
    q = deque([i])
    visited = [0]*(n+1)
    visited[i] = 1
    count = 1
    while q:
        v = q.popleft()
        # 다음 확인 요소 check 과정
        for j in graph[v]:
            if visited[j] == 0:
                visited[j] = 1
                count += 1
                q.append(j)  # q에 붙어있는거 대기로 붙임
    if count > max_value:
        max_value = count
        result = [i]
    elif count == max_value:
        result.append(i)
        max_value = count

for e in result:
    print(e, end=' ')
