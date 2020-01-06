n = int(input())
rope = []
for i in range(n):
    m = int(input())
    rope.append(m)

rope.sort()

result = []

for i in range(len(rope)):  # 0,1
    result.append(rope[i]*(n-i))
print(max(result))
