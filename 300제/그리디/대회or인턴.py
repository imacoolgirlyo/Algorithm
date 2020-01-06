N, M, K = map(int, input().split())
total = N+M

i = N // 2  # 3
j = M  # 3

max_team_num = min(i, j)

while True:
    if total-(2*max_team_num+max_team_num) >= K:
        print(max_team_num)
        exit(0)
    max_team_num -= 1
