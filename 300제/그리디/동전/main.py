N, K = map(int, input().split())
money = list()
for _ in range(N):
    n = int(input())
    money.append(n)

result = 0
num = K


while num > 0:
    mx = 0
    for i in money:
        if i <= num:
            if i > mx:
                mx = i
        else:
            break
    mok = num // mx  # 4200 // 1000
    result += mok  # 4
    num = num - (mx*mok)


print(result)
