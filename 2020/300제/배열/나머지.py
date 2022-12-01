obj = dict()
for i in range(0, 10):
    v = int(input())
    calc = v % 42
    if calc not in obj:
        obj[calc] = 1
    else:
        obj[calc] += 1

print(len(obj.keys()))
