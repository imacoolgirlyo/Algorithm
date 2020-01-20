from collections import deque

m, n = map(int, input().split())
farm = []
max_num = 1
tomato = deque([])
unriped = 0

for i in range(n):
    farm.append(list(map(int, input().split(' '))))
    for j in range(m):
        if farm[i][j] == 1:
            tomato.append((i, j))
        elif farm[i][j] == 0:
            unriped += 1


while tomato:
    x, y = tomato.popleft()
    ranged_arr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dx, dy in ranged_arr:
        nx, ny = x + dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if farm[nx][ny] != 0:
            continue
        tomato.append((nx, ny))
        farm[nx][ny] = farm[x][y] + 1
        max_num = max(farm[nx][ny], max_num)
        unriped -= 1

if unriped == 0:
    print(max_num-1)
else:
    print(-1)
