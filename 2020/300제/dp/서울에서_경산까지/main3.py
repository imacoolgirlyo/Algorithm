def solution(K, travel):
    n = len(travel)

    memo = [[0 for j in range(K+1)] for x in range(n+1)]

    for i in range(1, n+1):
        t_walk, v_walk, t_bike, v_bike = travel[i-1]

        for j in range(K+1):
            # walk
            if j >= t_walk:
                walk = memo[i-1][j-t_walk]+v_walk
            else:
                walk = 0

            bike = memo[i-1][j-t_bike]+v_bike if j >= t_bike else 0

            memo[i][j] = max(walk, bike)
    print(memo)
    return memo[n][K]


print(solution(1650, [[500, 200, 200, 100], [
      800, 370, 300, 120], [700, 250, 300, 90]]))
