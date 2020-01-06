n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    for j in range(0, 3):  # 0
        v = 10000
        for k in range(0, 3):  # 1,2
            if j != k:
                v = min(dp[i-1][k], v)
        dp[i][j] = v + arr[i][j]
    # dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    # dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    # dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

# print(dp)
print(min(dp[n-1]))

# [[26, 40, 83], [89, 86, 83], [96, 172, 185]]
# 96
