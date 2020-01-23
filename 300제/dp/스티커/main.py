test_case = int(input())

for _ in range(test_case):
    n = int(input())
    arr = []
    for t in range(2):
        arr.append(list(map(int, input().split())))

    dp = [[0]*n for _ in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    for i in range(1, n):
        if i <= 1:
            dp[0][i] = arr[0][i] + arr[1][i-1]
            dp[1][i] = arr[1][i] + arr[0][i-1]
        else:  # 2, 3
            v = max(dp[0][i-2], dp[1][i-2])
            dp[0][i] = max(arr[0][i]+dp[1][i-1], arr[0][i]+v)
            dp[1][i] = max(arr[1][i]+dp[0][i-1], arr[1][i]+v)

    print(max(dp[0][n-1], dp[1][n-1]))
