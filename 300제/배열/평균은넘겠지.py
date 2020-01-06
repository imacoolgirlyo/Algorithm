test_case = int(input())

for _ in range(test_case):
    score = list(map(int, input().split(' ')))
    total_num = score[0]
    result = 0
    mean = 0
    count = 0

    for i in range(1, total_num+1):
        result += score[i]

    mean = result/total_num

    for i in range(1, total_num+1):
        if score[i] > mean:
            count += 1

    result = (count/total_num)*100
    print("{0:.3f}%".format(result))
