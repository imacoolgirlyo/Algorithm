N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    temp = 100010
    if i % 6 == 0:
        temp = min(dp[i//3], dp[i//2])
    if i % 3 == 0:
        temp = min(dp[i//3], temp)
    elif i % 2 == 0:
        temp = min(dp[i//2], temp)
    temp = min(dp[i-1], temp)
    dp[i] = temp+1


print(dp[N])
