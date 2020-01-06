N, K = map(int, input().split())
jews = []
bags = []
for _ in range(N):
    M, V = map(int, input().split())
    jews.append([M, V, 0])

for _ in range(K):
    bags.append(int(input()))

bags.sort()
jews = sorted(jews, key=lambda x: x[0])

# for bagW in bags: # 2, 10
#   v = 0
#   for jew in jews: # (1,65)
#     if jew[0] <= bagW and jew[2] == 0:
#       v = max(v, jew[1])
