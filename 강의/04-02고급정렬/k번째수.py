n, k = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))

arr = sorted(arr)

for i in range(len(arr)):
    me = i+1
    if me == k:
        print(arr[i])
