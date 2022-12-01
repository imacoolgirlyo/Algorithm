n = int(input())
numbers = list()
for i in range(n):
    v = int(input())
    numbers.append(v)  # numbers.append(int(input()))

numbers.sort()

for i in numbers:
    print(i)

# 선택 정렬 알고리즘 사용: 0의 위치 부터 차례로 제일 작은 원소 가져옴
n = int(input())
numbers = list()
for i in range(n):
    numbers.append(int(input()))

for i in range(0, n):
    for j in range(i+1, n):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
