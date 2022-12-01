# from heapq import heappush, heappop

# n = int(input())
# heap = []

# for _ in range(n):
#     num = int(input())
#     if num == 0:
#         if heap:
#             print(heappop(heap))
#         else:
#             print(0)
#     else:
#         heappush(heap, num)

from heapq import heappush, heappop

n = int(input())
heap = []
result = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if heap:
            # print(heappop(heap))
            result.append(heappop(heap))
        else:
            result.append(0)
    else:
        heappush(heap, num)

for i in result:
    print(i)
