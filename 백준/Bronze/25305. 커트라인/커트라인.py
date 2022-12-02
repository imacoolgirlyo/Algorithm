candidates, awards = list(map(int, input().split(' ')))
list = list(map(int, input().split(' ')))


list.sort(reverse=True)
print(list[awards-1])
