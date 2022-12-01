from collections import deque

m, n, t = map(int, input().split())

farm = []
visited = [[[0]*m for _ in range(n)] for v in range(t)]
date = [[[0]*m for _ in range(n)] for v in range(t)]
unriped = 0
max_date = 0
q = deque([])

for _ in range(t):
    arr = []
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    farm.append(arr)

for i in range(t):
    for j in range(n):
        for k in range(m):
            if farm[i][j][k] == 1 and not visited[i][j][k]:
                q.append((i, j, k))
            if farm[i][j][k] == 0:
                unriped += 1


ranged_arr = [(-1, 0, 0), (1, 0, 0), (0, -1, 0),
              (0, 1, 0), (0, 0, -1), (0, 0, 1)]

while q:
    d, h, w = q.popleft()
    for dd, dh, dw in ranged_arr:
        nd, nh, nw = d+dd, h+dh, w+dw
        if nd < 0 or nd >= t or nh < 0 or nh >= n or nw < 0 or nw >= m:
            continue
        if farm[nd][nh][nw] == 0 and not visited[nd][nh][nw]:
            unriped -= 1
            visited[nd][nh][nw] = 1
            q.append((nd, nh, nw))
            date[nd][nh][nw] = date[d][h][w] + 1
            max_date = max(max_date, date[nd][nh][nw])

if max_date == 0:
    print(0)
elif unriped > 0:
    print(-1)
else:
    print(max_date)
