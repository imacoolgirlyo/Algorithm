a, b = map(str, input().split())

i = 0
count = 50
while i+len(a)-1 < len(b):  # 0+6-1 < 7
    string = b[i:i+len(a)]
    diff_count = 0
    for j in range(len(a)):
        if a[j] != string[j]:
            diff_count += 1
    count = min(count, diff_count)
    i += 1

print(count)
