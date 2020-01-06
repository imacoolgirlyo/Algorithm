n = int(input())
dp = [[0]*(n+1) for _ in range(n)]
arr = []

for i in range(n):  # 0,1,2,
    li = list(map(int, input().split()))
    arr.append(li)

dp[0][1] = arr[0][0]

for i in range(1, n):
    for j in range(1, len(arr[i])+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j-1]

print(max(dp[n-1]))
