dial = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5,
        'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}

s = input()
result = 0

for i in s:
    for key, value in dial.items():
        if i in key:
            result += value+1
            # print(result)

print(result)
