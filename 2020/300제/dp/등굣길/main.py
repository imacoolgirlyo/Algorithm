def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in puddles:
        x, y = i
        dp[y][x] = -1  # 조심!!!!!!!!!!!

    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007

    return dp[n][m]


print(solution(4, 3, [[2, 2]]))
