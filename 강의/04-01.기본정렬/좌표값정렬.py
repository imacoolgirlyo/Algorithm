n = int(input())
array = []

for i in range(n):
    x, y = list(map(int, input().split(' ')))
    array.append((x, y))

array = sorted(array, key=lambda el: [el[0], el[1]])

for i in array:
    print(i[0], i[1])
