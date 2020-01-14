R, C = map(int, input().split())
result = 0
Map = []
visited = [[False]*C for _ in range(R)]

for _ in range(R):
    li = list(input())
    Map.append(li)


def dfs(x, y):
    visited[x][y] = True
    if y == C-1:
        return 1
    if x-1 >= 0 and y+1 < C:
        if Map[x-1][y+1] == '.' and visited[x-1][y+1] == False:
            ans = dfs(x-1, y+1)
            if ans == 1:
                return 1
    if y+1 < C:
        if Map[x][y+1] == '.' and visited[x][y+1] == False:
            ans = dfs(x, y+1)
            if ans == 1:
                return 1
    if x+1 < R and y+1 < C:
        if Map[x+1][y+1] == '.' and visited[x+1][y+1] == False:
            ans = dfs(x+1, y+1)
            if ans == 1:
                return 1
    return 0


for i in range(R):
    result += dfs(i, 0)

print(result)
