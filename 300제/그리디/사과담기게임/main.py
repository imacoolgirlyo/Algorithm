n, m = map(int, input().split())
k = int(input())

result = 0
left = 1
right = left + m - 1

for _ in range(k):
    i = int(input())
    if i >= left and i <= right:
        continue
    elif i < left:
        diff = left - i
        result += diff
        left -= diff
        right -= diff
    elif i > right:
        diff = i-right
        result += diff
        right += diff
        left += diff

print(result)
