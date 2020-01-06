n = int(input())
arr = list()
result = 1

for i in range(n):
    k = list(map(int, input().split()))
    arr.append(k)

arr.sort(key=lambda x: (x[1], x[0]))
# print(arr)
t = arr[0][1]  # 4
for i in range(1, len(arr)):
    if t <= arr[i][0]:
        # print(i)
        result += 1
        t = arr[i][1]

print(result)
