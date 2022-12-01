n = int(input())
students = list()
for i in range(n):
    stu = list(input().split(' '))
    # 과연 시간 복잡도에 크게 영향을 미칠까? array 추가는 O(1)
    students.append([int(stu[0]), stu[1]])

# sorted는 원본을 건들지 않는다.
array = sorted(students, key=lambda student: student[0])

for student in array:
    print(student[0], student[1])

# 내 코드는 시간이 4168ms 소요 되었는데 318ms인 코드는 어디서 복잡도를 줄였을까?
# 해설과 동일한 방법으로 풀긴함
