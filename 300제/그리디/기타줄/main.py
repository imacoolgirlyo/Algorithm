# # 1번째 시도) 이 문제 쉽지 않다. -> 2번째 시도) 쉬움..;;
import math
n, m = map(int, input().split())
pkgArr = []
oneArr = []

for _ in range(m):
    pkg, one = map(int, input().split())
    pkgArr.append(pkg)
    oneArr.append(one)

min_pkg = min(pkgArr)
min_one = min(oneArr)

if n <= 6:
    print(min(min_pkg, n*min_one))
else:
    print(min(math.ceil(n/6)*min_pkg, n*min_one, (n//6)*min_pkg+(n % 6)*min_one))
