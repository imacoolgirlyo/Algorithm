st = list(input().split('-'))  # 55
result = 0
for i in range(len(st)):
    st_splited = st[i].split('+')
    r = 0
    for j in st_splited:
        r += int(j)
    if i == 0:
        result += r
    else:
        result -= r

print(result)
