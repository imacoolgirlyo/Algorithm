n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))


def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:
            now = array[i]
            result += 1
    return result


print(ascending(arr))
arr.reverse()
print(ascending(arr))
