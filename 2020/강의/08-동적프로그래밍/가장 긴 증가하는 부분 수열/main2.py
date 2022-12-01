
n = int(input())
arr = list(map(int, input().split()))
dp = [[0]*n for _ in range(n)]

for i in range(n):
    max_num = arr[i]
    for j in range(n):
        if i == j:
            dp[i][j] = 1
        if i < j:
            if max_num < arr[j]:
                max_num = arr[j]
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1]


print(max(map(max, dp)))
