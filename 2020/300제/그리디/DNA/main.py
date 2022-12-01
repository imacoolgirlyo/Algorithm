N, M = map(int, input().split())
DNAs = list(input() for _ in range(N))
total_str = [{} for _ in range(M)]
res_str = ''
res_num = 0

for i in range(N):  # TATGATAC 0 ~ 4
    for j in range(M):  # T, A, 0 ~ 7
        if DNAs[i][j] not in total_str[j]:
            total_str[j][DNAs[i][j]] = 1
        else:
            total_str[j][DNAs[i][j]] += 1


for i in range(len(total_str)):
    arr = sorted(total_str[i].items(),
                 key=lambda x: (-x[1], x[0]))
    st, nu = arr[0]
    res_str += st
    res_num += N-nu

print(res_str)
print(res_num)
