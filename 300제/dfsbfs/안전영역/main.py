import copy
import sys
sys.setrecursionlimit(10**8)

n = int(input())

result = 1  # 계속 틀린 point... 아무 지역도 비가 안왔을 때는 전체 한 뭉텅이기 때문에 초기값 1
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

max_h = max(max(x) for x in arr)
ranged_arr = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dfs(x, y, new_arr):
    visited[x][y] = 1

    for dx, dy in ranged_arr:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if new_arr[nx][ny] != -1 and not visited[nx][ny]:
            dfs(nx, ny, new_arr)

    return


for i in range(1, max_h+1):  # 채울 물의 양 설정
    new_arr = copy.deepcopy(arr)

    for x in range(n):  # 해당 물의 양에 따라 잠긴 곳 -1 처리해주기.
        for y in range(n):
            if new_arr[x][y] <= i:
                new_arr[x][y] = -1

    visited = [[0]*n for _ in range(n)]
    grp_total = 0

    for v in range(n):  # 본격적으로 구역 찾기. 잠기지 않고, 방문하지 않은 곳
        for w in range(n):
            if new_arr[v][w] != -1 and not visited[v][w]:
                grp_total += 1
                dfs(v, w, new_arr)

    result = max(grp_total, result)

print(result)
