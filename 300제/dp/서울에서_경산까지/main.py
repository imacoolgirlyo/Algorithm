def solution(K, travel):
    maxV = 0
    N = len(travel)

    def trip(i, time, money):
        global N, K, travel, maxV
        if time > K:
            return
        if i == N:
            if money > maxV:
                maxV = money
            return
        trip(i+1, time+travel[i][0], money+travel[i][1])
        trip(i+1, time+travel[i][2], money+travel[i][3])

    trip(0, 0, 0)
    print(maxV)


print(solution(1650, [[500, 200, 200, 100], [
      800, 370, 300, 120], [700, 250, 300, 90]]))
