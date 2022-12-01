test_case = int(input())

for _ in range(test_case):
    str_list = list(input())
    result = 0
    add = 0
    for i in str_list:
        if i == 'O':
            add += 1
            result += add
        else:
            add = 0
    print(result)
