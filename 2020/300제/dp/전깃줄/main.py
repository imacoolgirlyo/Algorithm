n = int(input())
dp = [1]*n
arr = []

for i in range(n):
    A, B = map(int, input().split())
    arr.append([A, B])

arr = sorted(arr, key=lambda x: x[0])

for i in range(n):
    for j in range(0, i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[j]+1, dp[i])

print(n-max(dp))
