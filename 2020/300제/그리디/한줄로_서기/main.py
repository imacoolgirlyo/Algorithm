n = int(input())
count = [-1]
a = list(map(int, input().split()))
result = [0]*(n+1)

for i in a:
    count.append(i)

for i in range(1, n+1):
    j = 1
    cnt = 0
    while True:
        if result[j]:
            j += 1
            continue

        if cnt == count[i]:
            result[j] = i
            break
        j += 1
        cnt += 1

for i in range(1, n+1):
    print(result[i], end=' ')
