n = int(input())
arr = sorted(list(map(int, input().split())))
res = 0
for i in range(0, len(arr)-1):
    if i == 0:
        if arr[0] != 1:
            break
    res += arr[i]
    if res+1 < arr[i+1]:  # 21 < 30, res = 20
        break

if res+1 < arr[len(arr)-1]:  # 21 < 30
    print(res+1)
else:  # 21 >= 21
    print(arr[len(arr)-1]+1)
