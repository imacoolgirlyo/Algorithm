#natural_generated_num = set(range(1, 10001))
# generated_num = set()

# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     generated_num.add(i)


# self_generated_num = natural_generated_num - generated_num

# for i in sorted(self_generated_num):
#     print(i)

# list = []
# for i in range(1, 10001):
#     list.append(i+sum(int(j) for j in str(i)))

# self_num = set(range(1, 10001)) - set(list)

# for i in sorted(self_num):
#     print(i)

list = []
for i in range(1, 10001):
    list.append(i + sum(int(j) for j in str(i)))

for i in range(1, 10001):
    if i not in list:
        print(i)
