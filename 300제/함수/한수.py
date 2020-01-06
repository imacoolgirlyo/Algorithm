N = int(input())
result = 0

if N < 100:
    result = N
else:
    result = 99
    for i in range(100, N+1):
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            result += 1


print(result)
