test_case = int(input())

for _ in range(test_case):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    arr = sorted(arr, key=lambda x: x[0])

    count = 1
    max_n = arr[0][1]  # 4
    for i in range(1, n):
        if arr[i][1] < max_n:
            count += 1
            max_n = arr[i][1]
    print(count)
