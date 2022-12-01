n = int(input())
n_list = list(map(int, input().split(' ')))
m = int(input())
m_list = list(map(int, input().split(' ')))

n_dic = {}
for i in n_list:
    n_dic[i] = True

for j in m_list:
    if j in n_dic:
        print(1)
    else:
        print(0)
