n = int(input())
arr = list(map(int, input().split()))
dp_inc = [1]*n
dp_dec = [1]*n


for i in range(1, n):
    for j in range(0, i):
        if arr[i] < arr[j]:
            dp_dec[i] = max(dp_dec[j]+1, dp_inc[j]+1, dp_dec[i])
        elif arr[i] > arr[j]:
            dp_inc[i] = max(dp_inc[j]+1, dp_inc[i])

print(max(max(dp_dec), max(dp_inc)))
