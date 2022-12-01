A, B = list(map(int, input().split(' ')))


def change(num):
    string = str(num)
    result = string[2]+string[1]+string[0]
    return int(result)


print(max(change(A), change(B)))

# a, b = map(list, map(str, input().split()))
# print(a, b)

# a.reverse()
# b.reverse()

# a_reverse = "".join(a)
# b_reverse = "".join(b)

# print(max(a_reverse, b_reverse))

# 345 678
# A, B = [3,4,5] [6,7,8]

# map(list, map(int, input().split()))
