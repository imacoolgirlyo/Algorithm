a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
obj = dict()

for i in result:
    if i not in obj:
        obj[i] = 1
    else:
        obj[i] += 1

for i in range(0, 10):
    string = str(i)
    if string not in obj:
        print(0)
    else:
        print(obj[string])
