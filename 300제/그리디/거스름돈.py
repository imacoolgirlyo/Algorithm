n = int(input())
money = [500, 100, 50, 10, 5, 1]
result = 0

rest = 1000-n
for i in money:
    if i <= rest:
        mok = rest//i
        rest = rest-(i*mok)
        result += mok

print(result)
