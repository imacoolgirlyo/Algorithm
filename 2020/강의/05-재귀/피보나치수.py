# n = int(input())

# a, b = 0, 1

# while n > 0:
#     a, b = b, a+b
#     n -= 1

# print(a)

n = int(input())  # 2
dp = [0]*(n+1)  # [0,1,2]

# print(dp)
for i in range(n+1):  # 0,1,2
    if i == 0 | i == 1:
        dp[i] = i
    else:
        dp[i] = dp[i-1]+dp[i-2]

print(dp[n])
