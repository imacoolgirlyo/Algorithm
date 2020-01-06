N = int(input())
score = list(map(int, input().split(' ')))
max_score = max(score)
result = 0

for i in score:
    value = (i/max_score) * 100
    result += value

print(result/N)
