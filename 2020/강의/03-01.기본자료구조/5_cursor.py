test_case = int(input())

for _ in range(test_case):
    leftStack = []
    rightStack = []
    data = input()
    for i in data:
        if i == '-':
            if leftStack:
                leftStack.pop()
        elif i == '<':
            if leftStack:
                rightStack.append(leftStack.pop())
        elif i == '>':
            if rightStack:
                leftStack.append(rightStack.pop())
        else:
            leftStack.append(i)
    leftStack.extend(reversed(rightStack))
    print(''.join(leftStack))
