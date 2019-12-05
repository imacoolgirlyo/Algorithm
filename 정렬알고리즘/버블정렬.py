def bubble_sort(lst):
    for num in range(len(lst)-1):
        swap = False
        for idx in range(len(lst)-num-1):
            if lst[idx] > lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                swap = True
        if swap == False:
            break
    return lst


print(bubble_sort([5, 2, 3, 1]))
