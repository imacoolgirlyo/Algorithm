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

print(tree)


def dfs(data):
    global result
    visited[data] = 1
    print(data)
    if len(tree[data]) == 1 and visited[tree[data][0]]:  # target이거나 target의 자식들은 이곳에 오지 못함
        result += 1
        return
    for child in tree[data]:
        if not visited[child] and child != target:
            dfs(child)
    return


if root != target:
    dfs(root)
    print('result', result)
else:
    print(0)
