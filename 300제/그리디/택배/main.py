n, c = map(int, input().split())
m = int(input())
info = []
cur_box = [0]*(n+1)  # 받는 애
result = 0

for _ in range(m):
    li = list(map(int, input().split()))
    info.append(li)

info1 = sorted(info, key=lambda x: (x[0], x[1]))
print(info1)
info2 = sorted(info, key=lambda x: (x[1], x[0]))
print(info2)
# cur_vil = 1

# while cur_vil < n+1:

#     if cur_box[cur_vil] > 0:  # 받는 과정
#         c += cur_box[cur_vil]
#         result += cur_box[cur_vil]
#         cur_box[cur_vil] = 0

#     for cur_info in info:  # 보내는 과정
#       # cur_info[0] :  보내는 곳, cur_info[1] : 받는 곳
#         if cur_info[0] != cur_vil:
#             continue

#         if c > 0 and cur_info[0] == cur_vil:
#             if c >= cur_info[2]:
#                 c -= cur_info[2]
#                 cur_box[cur_info[1]] += cur_info[2]
#             else:
#                 cur_box[cur_info[1]] += c
#                 c -= c

#     cur_vil += 1

print(result)
