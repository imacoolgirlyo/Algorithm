n = int(input())
dp = [{} for i in range(n+1)]

dp[1] = {'1': '1'}
dp[2] = {'00': '00', '11': '11'}
cur = 3

while cur <= n:
    # dp[cur] = [] 에 값을 넣
    for i in range(1, cur):  # 1,2,n-1
        j = cur-i
        for icur in dp[i].values():
            for jcur in dp[j].values():
                sum_str = icur+jcur
                if sum_str not in dp[cur]:
                    dp[cur][sum_str] = sum_str
    cur += 1

print(len(dp[n].values()) % 15746)
# print(len(dp[n]) % 15746)
