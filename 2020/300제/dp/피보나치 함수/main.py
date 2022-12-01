import sys
test_case = int(sys.stdin.readline())

dp = [[0]*2 for _ in range(0, 41)]

# dp[0][0] = 1
# dp[0][1] = 0
# dp[1][0] = 0
# dp[1][1] = 1

dp[0] = [0, 1]
dp[1] = [1, 0]

for i in range(2, 41):
    for j in range(0, 2):
        dp[i][j] = dp[i-2][j] + dp[i-1][j]


for _ in range(test_case):
    k = int(sys.stdin.readline())
    print(dp[k][0], dp[k][1])
