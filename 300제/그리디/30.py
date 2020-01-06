n = int(input())
n_list = sorted(str(n), reverse=True)
result = 0

if n_list[-1] != '0':
    print(-1)
else:
    for i in n_list:
        result += int(i)
    if result % 3 == 0:
        print(''.join(n_list))
    else:
        print(-1)
