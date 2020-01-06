n = int(input())
m = list(map(int, input().split(' ')))

i_num = 0
result = 0

for i in sorted(m):
    i_num += i  # 1, 1+2, 1+2+3
    result += i_num

print(result)
