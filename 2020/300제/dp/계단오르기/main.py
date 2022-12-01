N = int(input())
arr = [0]
dp = [0] * (N+1)
for _ in range(N):
    arr.append(int(input()))


for i in range(1, N+1):
    if i == 1:
        dp[i] = arr[1]
    elif i == 2:
        dp[i] = arr[1]+arr[2]
    else:
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

print(dp[N])

print('arr', arr)
print('dp', dp)

# arr [0, 10, 20, 15, 25, 10, 20]
# dp [0, 10, 30, 35, 55, 65, 75]
