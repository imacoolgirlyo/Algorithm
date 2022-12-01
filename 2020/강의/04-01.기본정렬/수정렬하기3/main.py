import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    array[num] += 1

for i in range(10001):
    for j in range(array[i]):
        print(i)
