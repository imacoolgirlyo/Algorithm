import string
s = list(input())
string_dict = dict()
for i in range(len(s)):
    if s[i] not in string_dict:
        string_dict[s[i]] = i

for i in list(string.ascii_lowercase):
    add = 0
    if i in string_dict:
        add = string_dict[i]
    else:
        add = -1
    print(add, end=" ")
