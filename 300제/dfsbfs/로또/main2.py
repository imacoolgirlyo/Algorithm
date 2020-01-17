# using backtracking

# 1 2 3 4 5 6
# 1 2 3 4 5 7
# 1 2 3 4 6 7
# 1 2 3 5 6 7
# 1 2 4 5 6 7
# 1 3 4 5 6 7
# 2 3 4 5 6 7


def re_lotto(n, T):
    for i in ranged_arr[n]:
        if i in T:
            continue

        if i < T[n-1]:
            continue
        if n < 5:
            T[n] = i
            re_lotto(n+1, T)
            T[n+1] = 0
            # print(T)
        else:
            print(' '.join(map(str, T[:-1])), end=' ')
            print(i)


def lotto():
    global ranged_arr
    for i in ranged_arr[0]:  # 1, 2
        T = [0]*6
        T[0] = i
        re_lotto(1, T)


while 1:
    arr = [*map(int, input().split())]
    # print(arr):  [7, 1, 2, 3, 4, 5, 6, 7], [8, 1, 2, 3, 5, 8, 13, 21, 34]
    if arr[0] == 0:
        break
    else:
        w = arr[0]-5
        ranged_arr = [arr[i+1:i+1+w] for i in range(6)]
        lotto()
    print()
