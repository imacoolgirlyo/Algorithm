docu = input()
string = input()
i = 0
result = 0

while len(docu)-i >= len(string):  # 0,1,
    if docu[i:i+len(string)] == string:
        i = i+len(string)
        result += 1
    else:
        i += 1

print(result)
