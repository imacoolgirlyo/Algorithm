num = int(input())
count = 0

for i in range(num):
    s = input()
    new_dict = dict()
    isGroup = True
    for j in range(0, len(s)):  # s[j] h, a , p , p y
        if s[j] in new_dict:
            if j-new_dict[s[j]] == 1:
                new_dict[s[j]] = j
            else:
                isGroup = False
        else:
            new_dict[s[j]] = j
    if isGroup:
        count += 1

print(count)
