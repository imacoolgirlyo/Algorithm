r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(map(int, input().split())))
result = ''

if r % 2:  # 세로가 홀수
    for i in range(r):
        for j in range(c-1):
            if i % 2 == 0:
                result += 'R'
            else:
                result += 'L'
        if i != r-1:
            result += 'D'

if c % 2 and r % 2 == 0:  # 가로가 홀수, 세로는 짝수
    for i in range(c):
        for j in range(r-1):
            if i % 2 == 0:
                result += 'D'
            else:
                result += 'U'
        if i != c-1:
            result += 'R'
minPos = (0, 0)
minScore = 1001

if c % 2 == 0 and r % 2 == 0:  # 둘 다 짝수
    for i in range(r):
        for j in range(c):
            if (i+j) % 2 and minScore > arr[i][j]:
                minPos = (i, j)
                minScore = arr[i][j]

print(minPos)
