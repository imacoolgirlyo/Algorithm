N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    res_3 = 100010
    res_2 = 100010
    res_mi = 100010
    if i % 3 == 0:
        res_3 = dp[i//3]+1
    elif i % 2 == 0:
        res_2 = dp[i//2]+1
    res_mi = dp[i-1]+1
    dp[i] = min(res_3, res_2, res_mi)


print(dp[N])
