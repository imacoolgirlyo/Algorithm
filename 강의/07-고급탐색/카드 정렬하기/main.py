import heapq
n = int(input())
heap = []

for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_v = one+two
    result += sum_v
    heapq.heappush(heap, sum_v)

print(result)
