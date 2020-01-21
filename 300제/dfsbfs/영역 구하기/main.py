import sys
sys.setrecursionlimit(10**8)
# 재귀 허용 깊이를 수동으로 설정해주지 않으면 런타임 에러가 난다.

m, n, k = map(int, input().split())
arr = [[0]*n for _ in range(m)]
visited = [[0]*n for _ in range(m)]
grp_cnt = 0
grp_sum = []
cnt = 0

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 1

ranged_arr = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = 1

    for dx, dy in ranged_arr:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if arr[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny)

    return cnt


for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and not visited[i][j]:
            grp_cnt += 1
            cnt = 0
            result = dfs(i, j)
            grp_sum.append(result)

grp_sum.sort()

print(grp_cnt)
for i in grp_sum:
    print(i, end=' ')
