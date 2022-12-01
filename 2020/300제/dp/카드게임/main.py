def solution(left, right):
    left_new = [0]
    right_new = [0]

    for i in left:
        left_new.append(i)

    for i in right:
        right_new.append(i)

    dp = [[0]*(len(right)+1) for _ in range(len(left)+1)]

    for i in range(1, len(left)+1):
        for j in range(1, len(right)+1):
            max_value = 0
            if left_new[i] > right_new[j-1]:
                max_value = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            else:
                max_value = max(dp[i-1][j-1], dp[i-1][j])
            if left_new[i] > right_new[j]:
                dp[i][j] = max_value + right_new[j]
            else:
                dp[i][j] = max_value
    print(dp)
    return dp[len(left)][len(right)]


print(solution([3, 2, 5], [2, 4, 1]))
