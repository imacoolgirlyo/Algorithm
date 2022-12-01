n = int(input())  # 10000개
parentNode = [-1]*(n+1)
tree = {}
root = 0

for _ in range(n):  # 1) 트리 형태 만들기
    v, left, right = map(int, input().split(' '))
    tree[v] = [left, right]
    if left != -1:
        parentNode[left] = v
    if right != -1:
        parentNode[right] = v

for i in range(1, n+1):  # 2) 루트 노드 찾기
    if parentNode[i] == -1:
        root = i

level_min = [n]*(n+1)  # 3) 각 레벨의 최소, 최대 idx 저장
level_max = [0]*(n+1)
level = [0]*(n+1)
level[root] = 1
cur = 0


def in_order(key):
    global cur
    if tree[key][0] != -1:
        level[tree[key][0]] = level[key] + 1
        in_order(tree[key][0])

    cur += 1
    # key는 8  데이터
    # 현재 깊이는 4  = level[부모]+ 1
    if level_min[level[key]] > cur:
        level_min[level[key]] = cur
    if level_max[level[key]] < cur:
        level_max[level[key]] = cur

    if tree[key][1] != -1:
        level[tree[key][1]] = level[key] + 1
        in_order(tree[key][1])

    return


in_order(root)

result = 0
result_idx = 0

for i in range(1, n+1):
    diff = level_max[i]-level_min[i]+1
    if result < diff:
        result = diff
        result_idx = i

print(result_idx, result)
