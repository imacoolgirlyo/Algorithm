# merge sort


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

    return lst


n = int(input())
lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

arr = merge_sort(lst)

for i in arr:
    print(i)
