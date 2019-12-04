# n = int(input())
# string = str(n)
# array = sorted(string)
# array.reverse()

# # array = sorted(str(n))

# print(int(''.join(array)))

array = input()

for i in range(9, -1, -1):
    for j in array:
        if i == int(j):
            print(i, end='')
