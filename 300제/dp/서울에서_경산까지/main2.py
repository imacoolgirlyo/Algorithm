def solution(K, travel):
    dp = [[0]*4 for _ in range(len(travel))]
    dp[0] = travel[0]

    for i in range(1, len(travel)):
        # 도보 먼저
        walk_m = 0
        walk_t = 0

        if dp[i-1][0] + travel[i][0] <= K:
            walk_m = dp[i-1][1] + travel[i][1]
            walk_t = dp[i-1][0] + travel[i][0]
        if dp[i-1][2] + travel[i][0] <= K:
            if walk_m < dp[i-1][3]+travel[i][1]:  # 같은 경우는 고려하지 않았음..ㅠ
                walk_m = dp[i-1][3]+travel[i][1]
                walk_t = 2
        dp[i][0] = walk_t
        dp[i][1] = walk_m

        cycle_m = 0
        cycle_t = 0

        if dp[i-1][0] + travel[i][2] <= K:  # 도보, 사이클
            cycle_m = dp[i-1][1] + travel[i][3]
            cycle_t = dp[i-1][0] + travel[i][2]

        if dp[i-1][2] + travel[i][2] <= K:  # 사이클, 사이클
            if cycle_m < dp[i-1][3] + travel[i][3]:
                cycle_m = dp[i-1][3] + travel[i][3]
                cycle_t = 2

        dp[i][2] = cycle_t
        dp[i][3] = cycle_m

    return max(dp[len(travel)-1][1], dp[len(travel)-1][3])


# print(solution(3000, [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]))

# 틀린 풀이임
