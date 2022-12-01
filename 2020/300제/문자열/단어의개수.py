string_list = list(input().split(' '))
result = 0

for i in string_list:
    if len(i) > 0:
        result += 1

print(result)
