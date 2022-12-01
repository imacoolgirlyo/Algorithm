n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]
result_num = 0
result = []
cnt = 0

for _ in range(n):
    row = list(map(int, input()))
    graph.append(row)


def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] and not visited[nx][ny]:
            # print(cnt)
            dfs(nx, ny)

    return cnt


for i in range(n):  # 0,1,2
    for j in range(n):
        cnt = 0
        count = 0
        if graph[i][j] and not visited[i][j]:
            count = dfs(i, j)
        if count > 0:
            result_num += 1
            result.append(count)

print(result_num)
result.sort()
for e in result:
    print(e)
