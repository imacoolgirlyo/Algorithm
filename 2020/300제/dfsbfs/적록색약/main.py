n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

visited = [[0]*n for _ in range(n)]
res = 0
ranged_arr = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs_normal(x, y, v):
    visited[x][y] = 1
    for dx, dy in ranged_arr:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not visited[nx][ny] and arr[nx][ny] == v:
            dfs_normal(nx, ny, arr[nx][ny])
    return


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            res += 1
            dfs_normal(i, j, arr[i][j])

print(res, end=' ')

res = 0
visited = [[0]*n for _ in range(n)]


def dfs_RG(x, y, v):
    visited[x][y] = 1

    for dx, dy in ranged_arr:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if v == 'R' or v == 'G':
            if not visited[nx][ny] and arr[nx][ny] != 'B':
                dfs_RG(nx, ny, arr[nx][ny])
        if v == 'B':
            if not visited[nx][ny] and arr[nx][ny] == 'B':
                dfs_RG(nx, ny, arr[nx][ny])
    return


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            res += 1
            dfs_RG(i, j, arr[i][j])

print(res, end=' ')
