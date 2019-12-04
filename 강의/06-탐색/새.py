N = int(input())
rest = N
K = 1
result = 0

while rest > 0:
    if K > rest:
        K = 1
    rest = rest-K  # 14-1, 13-2, 11-3 , 8-4, 4-1 , 3-2, 1-1
    K += 1
    result += 1

print(result)
