k = int(input())
a = list(input().split())


def convertToStr(arr):
    str_result = ''
    for i in arr:
        str_result += str(i)
    return str_result


def find_max(k):
    result = [0 for i in range(k+1)]
    result[0] = 9
    min_num = 9

    for i in range(1, k+1):
        if a[i-1] == '<':
            for k in range(i-1, -1, -1):
                result[k] = result[k]-1
                min_num = min(result[k], min_num)
                if k > 0 and a[k-1] == '>':
                    break
            result[i] = result[i-1]+1
        else:
            result[i] = min_num - 1
            min_num -= 1

    return convertToStr(result)


def find_min(k):
    result = [0 for i in range(k+1)]
    result[0] = 0
    max_num = 0

    for i in range(1, k+1):
        if a[i-1] == '>':
            for k in range(i-1, -1, -1):
                result[k] += 1
                max_num = max(max_num, result[k])
                if k > 0 and a[k-1] == '<':
                    break
            result[i] = result[i-1]-1
        else:
            result[i] = max_num + 1
            max_num += 1

    return convertToStr(result)


print(find_max(k))
print(find_min(k))
