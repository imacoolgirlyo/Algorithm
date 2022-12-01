# 그리디 하게 접근하는 DFS 문제

R, C = map(int, input().split())
visited = [[0]*C for _ in range(R)]
arr = []
res = 0
for _ in range(R):
    arr.append(list(input()))


def DFS(y, x):
    # 오른쪽, 오른쪽 위, 오른쪽 아래로 갈 수 있으면 ㄱ. 매 단계에서 고려
    visited[y][x] = 1
    if x == C-1:
        return 1
    if y-1 >= 0 and y+1 < R and x+1 < C:
        if arr[y-1][x+1] == '.' and visited[y-1][x+1] == 0:
            DFS(y-1, x+1)
            # if ans:
            #     return 1
        if arr[y][x+1] == '.' and visited[y][x+1] == 0:
            DFS(y, x+1)
            # if ans:
            #     return 1
        if arr[y+1][x+1] == '.' and visited[y+1][x+1] == 0:
            DFS(y+1, x+1)
            # if ans:
            #     return 1

    return 0


for y in range(R):
    res += DFS(y, 0)

print(res)
