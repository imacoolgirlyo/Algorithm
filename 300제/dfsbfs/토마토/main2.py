# 풀이 출처 : https://upcount.tistory.com/19
import sys
import collections

input = sys.stdin.readline

M, N = map(int, input().split())

unriped = 0
farm = []
tomato = collections.deque([])

for i in range(N):
    farm.append(list(map(int, input().split())))
    for t in range(M):
        if farm[i][t] == 1:  # 익은 토마토
            tomato.append((i, t))
        elif farm[i][t] == 0:  # 익지 않은 토마토의 경우
            unriped += 1

days = 1
while tomato:  # 익은 토마토가 있다면
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    t = tomato.popleft()  # 제일 처음 것을 꺼낸다.
    x = t[0]
    y = t[1]

    for i in range(4):  # 우, 좌, 하, 상 순으로 토마토를 익힌다..
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= N or nx < 0 or ny >= M or ny < 0:  # 농장 범위가 넘어가면 다음으로..
            continue
        if farm[nx][ny] != 0:  # 이미 토마토가 익어있다면, 넘어가자.
            continue

        farm[nx][ny] = farm[x][y] + 1
        tomato.append((nx, ny))
        days = max(farm[nx][ny], days)
        unriped -= 1

if unriped == 0:
    print(days-1)
else:
    print(-1)
