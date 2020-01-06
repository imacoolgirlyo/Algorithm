n, m = map(int, input().split())

A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]

cnt = 0


def filp(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1-A[i][j]


def checkEquality():
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False
    return True


for i in range(0, n-2):
    for j in range(0, m-2):
        if A[i][j] != B[i][j]:
            filp(i, j)
            cnt += 1

if checkEquality():
    print(cnt)
else:
    print(-1)
