def calc(strs):
    re = str(1) + strs.replace(" ", "")
    result = eval(re)

    if result == 0:
        print(strs)
    return


def solve(a, st, N):

    next_num = a+1
    next_str = str(next_num)

    add_s = st + "+" + next_str
    # print(add_s)
    sub_s = st + "-" + next_str
    # print(sub_s)
    clue_s = st + " " + next_str
    # print(clue_s)

    if next_num == N:
        calc(add_s)
        calc(sub_s)
        calc(clue_s)
        return

    solve(next_num, add_s, N)  # 1+
    solve(next_num, sub_s, N)
    solve(next_num, clue_s, N)


print(solve(1, "1", 3))

# n = int(input())

# for i in range(n):
#     num = int(input())
#     solve(1, "", num)
