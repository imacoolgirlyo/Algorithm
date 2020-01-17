# 시간초과 답변....이미 한번 체크한 걸 다시 체크해서 그런가..
from collections import deque

m, n = map(int, input().split())
tomato = []
visited = [[0]*m for _ in range(n)]
date = [[0]*m for _ in range(n)]
max_num = 0

empty_pos = 0
already_mature = 0
not_mature = 0

for _ in range(n):
    row = list(map(int, input().split(' ')))
    tomato.append(row)


def bfs(v, w):
    global not_mature, max_num
    q = deque([[v, w]])
    visited[v][w] = 1

    while q:
        x, y = q.popleft()
        ranged_arr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dx, dy in ranged_arr:
            nx, ny = x + dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] and date[nx][ny] > date[x][y]+1:
                date[nx][ny] = min(date[nx][ny], date[x][y]+1)
                q.append([nx, ny])
                # 다시 nx,ny 자식들도 재검토해야댐.

            if tomato[nx][ny] == 0 and visited[nx][ny] == 0:
                not_mature += 1
                tomato[nx][ny] = 1
                visited[nx][ny] = 1
                date[nx][ny] = date[x][y] + 1
                max_num = max(max_num, date[nx][ny])
                q.append([nx, ny])


for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            continue
        if tomato[i][j] == 1 and visited[i][j] == 0:
            already_mature += 1
            bfs(i, j)
        if tomato[i][j] == -1:
            empty_pos += 1

if already_mature + empty_pos == (n*m):
    print(0)
elif already_mature + empty_pos + not_mature < (n*m):
    print(-1)
else:
    print(max_num)
