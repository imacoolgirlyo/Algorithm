n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

length = len(data)
result = 0

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum = data[i] + data[j] + data[k]
            if sum <= m:
                result = max(result, sum)

print(result)
