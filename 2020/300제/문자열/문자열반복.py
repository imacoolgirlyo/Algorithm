test_case = int(input())

for _ in range(test_case):
    test = list(input().split(' '))
    result = ''
    for i in test[1]:
        result += i*int(test[0])
    print(result)
