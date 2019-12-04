case = int(input())
stack = []
result = []

k = 1
for i in range(case):
    n = int(input())
    while k <= n:
        stack.append(k)
        result.append('+')
        k += 1
    if stack[-1] == n:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

for i in result:
    print(i)


# for i in range(case):
#     n = int(input())
#     k = 1
#     while k <= n:  # 1 <= 4
#         stack.append(k)
#         result.append('+')
#         k += 1
#         print(stack)
#     if stack[-1] == n:
#         stack.pop()
#         result.append('-')
#     else:
#         print('NO')
#         exit(0)
