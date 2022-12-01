n = int(input())
visited = [0]*n
root = -1
tree = [[] for _ in range(n)]
arr = list(map(int, input().split(' ')))
target = int(input())

result = 0

for i in range(n):
    if arr[i] == -1:
        root = i
    else:
        tree[arr[i]].append(i)
        tree[i].append(arr[i])


def dfs(data):
    global result
    visited[data] = 1
    isLeaf = True

    for c in tree[data]:
        if not visited[c] and c != target:  # 자식이 target이 아닐 때 해당 값으로 dfs 호출
            isLeaf = False
            dfs(c)
    if isLeaf:
        result += 1
    return


if root != target:
    dfs(root)
    print(result)
else:
    print(0)
