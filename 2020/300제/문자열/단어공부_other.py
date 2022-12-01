s = input()
s_dict = dict()
maxNum = 0

for i in s:  # a, b, S
    upper = i.upper()
    if upper not in s_dict:
        s_dict[upper] = 1
    else:
        s_dict[upper] += 1

maxNum = max(s_dict.values())
haveAnswer = False
result = ''
for key, value in s_dict.items():
    if value == maxNum:
        if(haveAnswer):
            result = '?'
        else:
            haveAnswer = True
            result = key

print(result)
