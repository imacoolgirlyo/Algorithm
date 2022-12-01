N, A = int(input()), sorted(list(map(int, input().split())))

ans = 0

for i in A:
    if i <= ans+1:  # 현재 값이, 지금까지 만들어 왔던 값 +1 클 때만 합쳐줌
        ans += i
    else:
        break

print(ans+1)
