n = int(input())
books = {}
result = []

for i in range(n):
    b = input()
    if b not in books:
        books[b] = 1
    else:
        books[b] += 1

max_book = max(books.values())

for b, v in books.items():
    if v == max_book:
        result.append(b)

print(sorted(result)[0])
